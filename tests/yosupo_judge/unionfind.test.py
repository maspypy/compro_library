# verify-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind
# @import graph/union_find.py
import sys
sys.path.insert(0, '.')

from graph.union_find import find_root, merge
import numpy as np


stdin = open(0)
data = np.fromstring(stdin.read(), np.int64, sep=' ')


def main(data):
    N, Q = data[:2]
    TUV = data[2:]
    T = TUV[::3]
    U = TUV[1::3]
    V = TUV[2::3]
    root = np.arange(N)
    size = np.ones(N, np.int64)
    for t, u, v in zip(T, U, V):
        if t == 0:
            merge(u, v, root, size)
        else:
            print(1 if find_root(u, root) == find_root(v, root) else 0)


main(data)
