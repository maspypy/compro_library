from numba import njit
import numpy as np


@njit('i8[:](i8[:],i8[:],b1)', cache=True)
def dirichlet_zeta_transform(A, primes, inplace=False):
    """Compute the zeta transform of A.

    Transform A to B. B[n] = sum_{d|n} A[d]

    Parameters
    ----------
    A : np.ndarray(dtype=np.int64)
        input array
    primes : np.ndarray(dtype=np.int64)
        Array of primes < len(A). This array can be computed by
        prime_table function in this module.
    inplace : bool, optional
        True if overwrite A, by default False
    """
    N = len(A) - 1
    if not inplace:
        A = A.copy()
    for p in primes:
        for i in range(1, N // p + 1):
            A[i * p] += A[i]
    return A


@njit('i8[:](i8[:],i8[:],b1)', cache=True)
def dirichlet_mobius_transform(A, primes, inplace=False):
    """Compute the zeta transform of A.

    Transform A to B. B[n] = sum_{d|n} A[d]modiub[n//d]

    Parameters
    ----------
    A : np.ndarray(dtype=np.int64)
        input array
    primes : np.ndarray(dtype=np.int64)
        Array of primes < len(A). This array can be computed by
        prime_table function in this module.
    inplace : bool, optional
        True if overwrite A, by default False
    """
    N = len(A) - 1
    if not inplace:
        A = A.copy()
    for p in primes:
        for i in range(N // p, 0, -1):
            A[i * p] -= A[i]
    return A


def sigma_0_table(N, primes):
    A = np.ones(N, np.int64)
    A[0] = 0
    return dirichlet_zeta_transform(A, primes, inplace=True)


def sigma_1_table(N, primes):
    A = np.arange(N, dtype=np.int64)
    return dirichlet_zeta_transform(A, primes, inplace=True)


def euler_phi_table(N, primes):
    A = np.arange(N, dtype=np.int64)
    return dirichlet_mobius_transform(A, primes, inplace=True)
