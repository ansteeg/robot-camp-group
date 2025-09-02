def solution_station_4(a: int, b: int) -> bool:
    if b % a == 0:
        return True
    if b > 1 and all(b % i for i in range(2, int(b**0.5) + 1)):
        return True
    return False
