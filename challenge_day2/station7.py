def solution_station_7(expr: str) -> float:
	# Evaluate simple algebraic expressions like 'a+b', 'b+c', 'd*e'
	# using the mapping derived from the station notes.
	values = {
		'a': 3.0,
		'b': -1.0,
		'c': 4.0,
		'd': 7.0,
		'e': 0.5,
	}
	left = expr[0]
	op = expr[1]
	right = expr[2]
	if op == '+':
		return float(values[left] + values[right])
	if op == '-':
		return float(values[left] - values[right])
	if op == '*':
		return float(values[left] * values[right])
	raise ValueError("Unsupported expression format")


