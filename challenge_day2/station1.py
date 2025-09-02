from functools import lru_cache

def _fib_fast_doubling(n: int):

    if n == 0:
        return (0, 1)
    a, b = _fib_fast_doubling(n >> 1)
    c = a * ((b << 1) - a)
    d = a*a + b*b
    if n & 1:
        return (d, c + d)
    else:
        return (c, d)

def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return _fib_fast_doubling(n)[0]

def solution_station_1():
    return fib(3)
