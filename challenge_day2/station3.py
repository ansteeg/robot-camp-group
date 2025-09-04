def solution_station_3(value: int) -> bool:
	# True if sum of digits divisible by 3
	digit_sum = sum(int(ch) for ch in str(value))
	return digit_sum % 3 == 0


