def solution_station_5(name: str) -> int:
	# Count enclosed holes in letters (both cases)
	holes_map = {
		'A': 1, 'a': 1,
		'B': 2, 'b': 1,
		'O': 1, 'o': 1,
		'P': 1, 'p': 1,
		'Q': 1, 'q': 1,
	}
	return sum(holes_map.get(ch, 0) for ch in name)


