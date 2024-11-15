import ctypes
myfib = ctypes.CDLL('./libfib.so')
fib = myfib.fib
fib.argtypes = [ctypes.c_int]
fib.restype = ctypes.c_long
from sys import argv
n = int(argv[1]) if len(argv) > 1 else 32
print(fib(n))

# time python3 fibrec.py 38 # 21.634 (50x C)
# time python3 cfib.py 38 # 1.142 (2.6x C)
# time ./fibrec 38 # 0.433
