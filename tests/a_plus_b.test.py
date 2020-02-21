# verify-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb
# @import compro_library/example_library/a_plus_b.py
from compro_library.example_library.a_plus_b import a_plus_b

a, b = map(int, input().split())
answer = a_plus_b(a, b)
print(answer)
