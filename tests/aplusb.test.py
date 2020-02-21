# verify-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb
# @import example_library/aplusb.py

import sys
sys.path.insert(0, '.')

from example_library.aplusb import aplusb

a, b = map(int, input().split())
answer = a + b
print(answer)
