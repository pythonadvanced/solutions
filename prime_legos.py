
##################################################
# prime_legos
##################################################
import itertools

def prime_legos():
    """
    iterates over shifted primes (with a 5-items padding with 1s)
    and over primes squares
    """
    part1 = itertools.chain(itertools.repeat(1, 5), primes())
    part2 = (prime**2 for prime in primes())
    return zip(part1, part2)


##################################################
# prime_legos_bis
##################################################
import itertools

def prime_legos_bis():
    """
    same behaviour
    we optimize CPU performance by creating a single instance
    of the primes() generator, and duplicate it using `itertools.tee()`
    """
    # this is where the pseudo-copy takes place
    primes1, primes2 = itertools.tee(primes(), 2)
    # the rest is of course the same as in the naive version
    part1 = itertools.chain(itertools.repeat(1, 5), primes1)
    part2 = (prime**2 for prime in primes2)
    return zip(part1, part2)

