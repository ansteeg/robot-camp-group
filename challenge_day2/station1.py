def solution_station_1(n):
    def fast_doubling(n: int):
        if n == 0:
            return (0, 1)
        a, b = fast_doubling(n >> 1)
        c = a * ((b << 1) - a)
        d = a*a + b*b
        if n & 1:
            return (d, c + d)
        else:
            return (c, d)
    if n < 0:
        raise ValueError("n must be nonnegative")
    return fast_doubling(n)[0]