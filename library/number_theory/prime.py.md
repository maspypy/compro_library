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
<script type="text/javascript" src="../../assets/js/copy-button.js"></script>
<link rel="stylesheet" href="../../assets/css/copy-button.css" />


# :heavy_check_mark: number_theory/prime.py

<a href="../../index.html">Back to top page</a>

* category: <a href="../../index.html#814c07620aec62314b2fd23fc462e282">number_theory</a>
* <a href="{{ site.github.repository_url }}/blob/master/number_theory/prime.py">View this file on GitHub</a>
    - Last commit date: 2020-02-22 13:47:05+09:00




## Verified with

* :heavy_check_mark: <a href="../../verify/tests/aizu_online_judge/euler_phi.test.py.html">tests/aizu_online_judge/euler_phi.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
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

<a href="../../index.html">Back to top page</a>

