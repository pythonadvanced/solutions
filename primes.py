
##################################################
# primes
##################################################
import math
import itertools

def primes():
    """
    enumerate prime numbers
    """
    # the set of primes we have found so far
    # so we avoid divisions by non-primes
    cache_primes = set()
    
    for n in itertools.count(2):
        for i in range(2, int(math.sqrt(n))+1):
            # no need to try to divide by non-primes
            if i not in cache_primes:
                continue
            # not a prime, go to n+1
            if n % i == 0:
                break
        # remember that a 'for' statement 
        # can be attached an 'else' which
        # gets executed when no 'break' statement has triggered
        # in our case, we run this 'else' part when n is prime
        else:
            # n is prime, remember it for the rest of the enumeration
            cache_primes.add(n)
            yield n

