#include <stdio.h>
 
long fib(int n) {
	if (n < 2)
		return n;
	return fib(n - 2) + fib(n - 1);

}

/* gcc -fPIC -shared -o libfib.so libfib.c

import ctypes
libfib = ctypes.CDLL('./libfib.so')
fib = libfib.fib
fib.argtypes = [ctypes.c_int]
fib.restype = ctypes.c_long
from sys import argv
print(fib(int(argv[1]) if len(argv) > 1 else 32))
*/
