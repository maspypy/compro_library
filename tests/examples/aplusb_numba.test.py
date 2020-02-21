# verify-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb
# @import example_library/aplusb_numba.py
import sys
sys.path.insert(0, '.')

from example_library.aplusb_numba import aplusb

a, b = map(int, input().split())
answer = aplusb(a, b)
print(answer)
