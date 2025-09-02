def solution_station_3(n: int) -> bool:
    # True als n een priemgetal is
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
