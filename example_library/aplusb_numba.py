from numba import njit


@njit
def aplusb(a, b):
    return a + b
