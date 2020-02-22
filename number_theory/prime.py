import numpy as np


def prime_table(N):
    """Create prime table of interval [0, N)

    Parameters
    ----------
    N : int
        Upper bound. N must be >= 2.

    Returns
    -------
    tuple of two arrays.
    is_prime: is_prime[i] = True iff i is prime.
    primes: primes[i] = (i+1)-th prime
    """
    is_prime = np.zeros(N, np.bool_)
    is_prime[2] = 1
    is_prime[3::2] = 1
    for p in range(3, N, 2):
        if p * p > N:
            break
        if is_prime[p]:
            is_prime[p * p::p + p] = 0
    primes = np.where(is_prime)[0]
    return is_prime, primes
