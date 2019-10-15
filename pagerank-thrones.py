#!/usr/bin/env python
# coding: utf-8

# # pagerank: a possible implementation

# *****

# ## getting data over http

# In[ ]:


# beware that requests is NOT is the standard library
# so you may need to run in the terminal:
# 
# $ pip install requests

import requests

# URL = "https://www.macalester.edu/~abeverid/data/stormofswords.csv"
# identical on github
URL = "https://raw.githubusercontent.com/pupimvictor/NetworkOfThrones/master/stormofswords.csv"


# In[ ]:


# GET contents using http
request = requests.get(URL)

csv = request.text


# In[ ]:


# csv is a str object
type(csv), len(csv)


# *****

# ## parsing

# ### splitting into lines

# In[ ]:


# how many lines
lines = csv.split("\n")
len(lines)


# ### a glimpse
# 
# this is to get a sense of the data we have got; we look at the first and last lines

# In[ ]:


# let's take a quick look at the 3 first lines
line1, line2, line3, *ignore = lines


# In[ ]:


# turns ou first line is a header
# that's expected in a csv file
line1


# In[ ]:


# then we get regular data
line2


# In[ ]:


line3


# In[ ]:


# same at the end
*ignore, line_2, line_1 = lines


# In[ ]:


line_2


# In[ ]:


# last line is empty
line_1


# ### meaningful lines : a slice

# In[ ]:


# we want to expose an iterable over meaningful lines
# (i.e. excluding the header line)
# so using a slice springs to mind

meaningful = lines[1:-1]


# *****

# ### building a programing-friendly data

# we need to turn this text object into something more programing-friendly  
# this stage is called *parsing*

# there is [a module called `csv` in the standard library](https://docs.python.org/3/library/csv.html), that could come in handy for more complex cases  
# but here things are so simple, let's parse this data "by hand"

# ### splitting a line in pieces: `str.split()`

# In[ ]:


for index, line in enumerate(meaningful):
    source, target, weight = line.split(',')
    if index < 3:
        print(f"{source} → {weight} → {target}")
    else:
        print('.', end='')


# ### building a dictionary (1)

# In[ ]:


# but let's build a dictionary of dictionaries instead
# for that we iterate over the (meningful) lines again
graph1 = {}
for line in meaningful:
    source, target, weight = line.split(',')
    if source not in graph1:
        graph1[source] = {}
    graph1[source][target] = weight


# In[ ]:


# so each value in the graph 
# in turn is a dictionary
graph1['Aemon']


# **NOTE** that in this first version, weights are stored as `str` objects; we'll improve this 

# ### building a dictionary (2)

# in fact there's a slightly better way to do this, as that fragment here 
# ```python
#     if source not in graph1:
#         graph1[source] = {}
# ```
# is not so nice; we can get rid of it by using a `defaultdict` object
# 
# `defaultdict` is a class that inherits the regular `dict` class;  
# a `defaultdict` of `list`s, for example, will automatically create a `list()` instance whenever one tries to access a missing key

# In[ ]:


# this is in the standard library, no need to pip install
from collections import defaultdict

# here our values are nested dicts
graph = defaultdict(dict)

for index, line in enumerate(meaningful):
    source, target, weight = line.split(',')
    # we take this chance to convert weight as an int
    graph[source][target] = int(weight)


# In[ ]:


graph['Aemon']


# *****

# ## simulator

# In[ ]:


import random

class PageRankWalker:
    

    def __init__(self, graph, damping=0.85):
        self.graph = graph
        self.damping = damping
        # the vertex we are on
        self.current = None
        self.init_random()
        

    def init_random(self):

        # for each vertex we prepare a 'bucket' 
        # that is to say a list of neighbour vertices
        # each appearing as many times as the outgoing weight
        # this way a random walk only needs to pick
        # randomly in that list using random.choice
        #
        # self.weighted_buckets is a dictionary that 
        # maps each vertex to its own bucket
        
        self.weighted_buckets = defaultdict(list)
        for source, links_dict in graph.items():
            # source_bucket is a list object
            source_bucket = self.weighted_buckets[source]
            for target, weight in links_dict.items():
                for _ in range(weight):
                    source_bucket.append(target)
                    
        # same for when we restart, we store in self.restart_bucket
        # a simple list of all the vertices; so using random.choice()
        # on this list will perform a fair pick
        # here we really need a list object as 
        # trying to random.choice() on a dict_keys object 
        # won't work
        self.restart_bucket = list(self.graph.keys())


    def pick_start_vertex(self):
        """
        randomly picks a start vertex
        with equal choices
        """
        return random.choice(self.restart_bucket)


    def pick_next_vertex(self):
        """
        randomly picks a successor from current vertex
        using the weights
        """
        choices = self.weighted_buckets[self.current]
        # when reaching a vertex with no outgoing edge
        # we restart from the beginning
        if not choices:
            return self.pick_start_vertex()
        else:
            return random.choice(choices)

        
    def walk(self, nb_steps):
        """
        simulates that number of steps
        result is a dictionary with vertices as key, 
        and as value number of steps spent in that vertex
        """
        result = defaultdict(int)

        # pick initial vertex
        self.current = self.pick_start_vertex()
        result[self.current] += 1

        # we've alredy done one step, so remove 1 here
        for _ in range(nb_steps-1):

            # restart or not based on damping
            # random.random() is uniform between 0. and 1.
            r = random.random()
            if r <= self.damping:
                self.current = self.pick_next_vertex()
            else:
                self.current = self.pick_start_vertex()
            # record where we are at this step
            result[self.current] += 1
            
        return result


# *****

# ### using the simulator

# In[ ]:


walker = PageRankWalker(graph)


# In[ ]:


# let's see what we get with that amount of steps

STEPS = 1000
frequencies = walker.walk(STEPS)


# In[ ]:


# the sum of all values should be STEPS
raincheck = sum(frequencies.values())
raincheck == STEPS == 1000


# let's show the top most frequent vertices

# In[ ]:


# dicts are not so good at sorting
# let's use a list instead
tuples = [(vertex, count) for vertex, count in frequencies.items()]

# now we can sort, using as a criteria the 'count' part in each tuple
tuples.sort(key = lambda tupl: tupl[1], reverse=True)

tuples[:5]


# #### note on `lambda`
# 
# we have not yet explained `lambda`, it will be during the course on functional objects
# 
# in a nutshell, these 2 cells are equivalent

# In[ ]:


# the lambda expression creates a function object on the fly
tuples.sort(key = lambda tupl: tupl[1], reverse=True)


# In[ ]:


# we could have created that function object 
# with a proper def: instead
def the_count_part(tupl):
    return tupl[1]

tuples.sort(key = the_count_part, reverse=True)


# ***

# make it reproducible

# In[ ]:


# walk the graph that many steps, 
# and diplay the top 4 most popular characters

def monte_carlo(graph, steps):
    walker = PageRankWalker(graph)
    frequencies = walker.walk(steps)
    # sort results to show most frequent first
    tuples = [ (vertex, count) for vertex, count in frequencies.items() ]
    tuples.sort(key = lambda tupl: tupl[1], reverse=True)
    # display 4 most frequents
    for character, count in tuples[:4]:
        print(f"{character} was visited {count} times i.e. {count/steps:02%}")


# In[ ]:


# run 5 times and display results
for _ in range(5):
    print(f"{40*'-'}")
    monte_carlo(graph, STEPS)


# In[ ]:


# what if we increase STEPS to 10000

STEPS = 10_000

for _ in range(5):
    print(f"{40*'-'}")
    monte_carlo(graph, STEPS)


# In[ ]:


# what if we increase STEPS to 1_000_000

STEPS = 1_000_000

for _ in range(5):
    print(f"{40*'-'}")
    monte_carlo(graph, STEPS)


# ***

# ### visualization (optional)

# using [the graphviz library](https://graphviz.readthedocs.io/en/stable/examples.html) 
# 
# installing dependencies is a 2-step process
# 
# * the binary tool; for that [see the project's page](https://graphviz.gitlab.io/download/);  
#   also be aware that most common linux distros do support *graphviz*,  
#   so you can install them with either `dnf` or `apt-get`;  
#   or `brew` if on MacOS
# 
# * the Python wrapper that you can install with (surprise !)
# ```bash
# pip install graphviz
# ```

# In[ ]:


# DiGraph stands for Directed Graph
# that's what we need since our graph is directed indeed

from graphviz import Digraph


# In[ ]:


gv = Digraph('Characters of the Thrones', filename='thrones.gv')

for source, weighted_dict in graph.items():
    for target, weight in weighted_dict.items():
        gv.edge(source, target, label=f"{weight}")


# In[ ]:


gv.attr(rankdir='TB', size='12')
gv

