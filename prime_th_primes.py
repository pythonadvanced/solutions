
##################################################
# prime_th_primes
##################################################
def prime_th_primes():
    """
    iterate the n-th prime number, with n it self being prime
    
    given that primes() emits 2, 3, 5
    then prime_th_primes() starts with 5 which has index 2 in that enumeration
    """
    primes1 = primes()
    primes2 = primes()
    
    # current will scan all prime numbers
    current = next(primes1)
    # index will scan all integers
    for index, prime in enumerate(primes2):
        # when it matches 'current' it means we have a winner
        if index == current:
            yield prime
            current = next(primes1)


##################################################
# prime_th_primes_bis
##################################################
def prime_th_primes_bis():
    """
    same purpose
    
    this approach is a little more manual
    as we do our own calls to next() 
    
    """
    primes1 = primes()
    primes2 = primes()
    # this start with -1 because it's a number of times we need to do next()
    # and, as opposed with usual indexing that starts at 0
    # to get item at index 0 we need to do ONE next()
    current_index = -1
    
    while True:
        # what's the next prime index
        next_index = next(primes1)
        # the amount of times we must iterate on primes2
        offset = next_index - current_index
        # move primes2 forward that many times
        for _ in range(next_index-current_index):
            output = next(primes2)
        # we have a winner
        yield output
        # this is where we are, so we can compute the next hop
        current_index = next_index

