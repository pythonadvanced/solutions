
##################################################
# prime_squares
##################################################
def prime_squares():
    """
    iterates over the squares of prime numbers
    """
    # a generator expression is the most obvious way that springs to mind
    return (prime**2 for prime in primes())


##################################################
# prime_squares_bis
##################################################
def prime_squares_bis():
    """
    same using a generator function
    """
    # a generator expression is the most obvious way that springs to mind
    for prime in primes():
        yield prime**2

