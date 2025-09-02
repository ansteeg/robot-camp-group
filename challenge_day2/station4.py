# station4.py

def solution_station_4(n):
    """
    Check if a number is prime.
    Returns True if prime, False otherwise.
    """
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:   # if divisible by i, not prime
            return False
    return True
