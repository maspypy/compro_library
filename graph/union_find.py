from numba import njit


@njit('i8(i8,i8[:])', cache=True)
def find_root(x, root):
    while root[x] != x:
        root[x] = root[root[x]]
        x = root[x]
    return x


@njit('b1(i8,i8,i8[:],i8[:])', cache=True)
def merge(x, y, root, size):
    x = find_root(x, root)
    y = find_root(y, root)
    if x == y:
        return False
    if size[x] < size[y]:
        root[x] = y
        size[y] += size[x]
    else:
        root[y] = x
        size[x] += size[y]
    return True
