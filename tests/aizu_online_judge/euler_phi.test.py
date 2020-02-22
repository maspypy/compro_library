# verify-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2286
# @import number_theory/prime.py
# @import number_theory/dirichlet_convolution.py
import sys
sys.path.insert(0, '.')

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np
from number_theory.prime import prime_table
from number_theory.dirichlet_convolution import euler_phi_table


U = 10**6 + 1
is_prime, primes = prime_table(U)
phi = euler_phi_table(U, primes)
A = phi.cumsum() + 1


T = int(readline())
N = np.array(read().split(), np.int32)
print(*A[N], sep='\n')
