def solution_station_4(n: int) -> bool:
	# True if n is prime
	if n < 2:
		return False
	if n % 2 == 0:
		return n == 2
	i = 3
	while i * i <= n:
		if n % i == 0:
			return False
		i += 2
	return True


