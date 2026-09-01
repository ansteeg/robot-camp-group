def solution_station_4(b: int) -> bool:
# Return True if b is a prime number, False otherwise.
    if b < 2:
        return False
    for i in range(2, int(b**0.5) + 1):
        if b % i == 0:
            return False
    return True
