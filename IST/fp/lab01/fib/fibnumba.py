#!/usr/bin/env python3
# https://numba.pydata.org/
# sudo pip3 install numba

from numba import jit
@jit(nopython=True)
def fib(n):
  if n < 2:
    return n
  return fib(n-2) + fib(n-1)

n=42
import sys
if len(sys.argv) > 1:
  n=int(sys.argv[1])
print ("fib(%d)=%d" % (n, fib(n)))
