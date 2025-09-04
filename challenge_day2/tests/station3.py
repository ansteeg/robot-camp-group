def solution_station_3(b: int) -> bool:
# Return True if the sum of digits of b is divisible by 3, else False.
    digit_sum = sum(int(d) for d in str(b))
    return digit_sum % 3 == 0
