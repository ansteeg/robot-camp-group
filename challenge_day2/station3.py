def solution_station_3(n: int) -> bool:
    """
    This function checks if a number is a Kaprekar number.
    """
    if n == 1:
        return True
    if n <= 0:
        return False

    sq_n = n * n
    s = str(sq_n)
    d = len(str(n))

    for i in range(1, len(s)):
        part1_str = s[:i]
        part2_str = s[i:]
        
        if not part1_str or not part2_str:
            continue

        part1 = int(part1_str)
        part2 = int(part2_str)

        if part1 > 0 and part2 > 0 and part1 + part2 == n:
            return True
            
    return False