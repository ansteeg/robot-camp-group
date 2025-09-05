def solution_station_1(n: int) -> int:
    """
    This function calculates the nth Fibonacci number.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b