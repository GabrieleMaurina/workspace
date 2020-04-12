import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return (n <=2 and 1) or fib(n-1) + fib(n-2)

print(fib(int(sys.argv[1])))
