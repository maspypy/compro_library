---
layout: default
---

<!-- mathjax config similar to math.stackexchange -->
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    TeX: { equationNumbers: { autoNumber: "AMS" }},
    tex2jax: {
      inlineMath: [ ['$','$'] ],
      processEscapes: true
    },
    "HTML-CSS": { matchFontHeight: false },
    displayAlign: "left",
    displayIndent: "2em"
  });
</script>

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery-balloon-js@1.1.2/jquery.balloon.min.js" integrity="sha256-ZEYs9VrgAeNuPvs15E39OsyOJaIkXEEt10fzxJ20+2I=" crossorigin="anonymous"></script>
<script type="text/javascript" src="../../../assets/js/copy-button.js"></script>
<link rel="stylesheet" href="../../../assets/css/copy-button.css" />


# :heavy_check_mark: tests/aizu_online_judge/euler_phi.test.py

<a href="../../../index.html">Back to top page</a>

* <a href="{{ site.github.repository_url }}/blob/master/tests/aizu_online_judge/euler_phi.test.py">View this file on GitHub</a>
    - Last commit date: 2020-02-23 02:23:48+09:00




## Depends on

* :heavy_check_mark: <a href="../../../library/number_theory/dirichlet_convolution.py.html">number_theory/dirichlet_convolution.py</a>
* :heavy_check_mark: <a href="../../../library/number_theory/prime.py.html">number_theory/prime.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
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

```
{% endraw %}

<a id="bundled"></a>
{% raw %}
```cpp
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.8.1/x64/lib/python3.8/site-packages/onlinejudge_verify/docs.py", line 348, in write_contents
    bundled_code = language.bundle(self.file_class.file_path, basedir=self.cpp_source_path)
  File "/opt/hostedtoolcache/Python/3.8.1/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/other.py", line 48, in bundle
    return subprocess.check_output(shlex.split(command))
  File "/opt/hostedtoolcache/Python/3.8.1/x64/lib/python3.8/subprocess.py", line 411, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
  File "/opt/hostedtoolcache/Python/3.8.1/x64/lib/python3.8/subprocess.py", line 512, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['false']' returned non-zero exit status 1.

```
{% endraw %}

<a href="../../../index.html">Back to top page</a>

