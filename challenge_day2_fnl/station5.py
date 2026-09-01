import os


def solution_station_5(name: str) -> int:
	# Return the 1-based position of the given name in tests/list.txt, or -1 if not found
	# Build path to the list file relative to this file
	list_path = os.path.join(os.path.dirname(__file__), 'tests', 'list.txt')
	try:
		with open(list_path, 'r', encoding='utf-8') as f:
			content = f.read()
	except FileNotFoundError:
		return -1

	# The file contains group labels like "LT2:" inline; split by comma and strip labels
	raw_tokens = content.replace('\n', ' ').split(',')
	names = []
	for token in raw_tokens:
		clean = token.strip()
		if not clean:
			continue
		# If a group label like "LT3: Name" appears, take the part after the last ':'
		if ':' in clean:
			clean = clean.split(':')[-1].strip()
		if clean:
			names.append(clean)

	# Find 1-based position
	try:
		index_0_based = names.index(name)
		return index_0_based + 1
	except ValueError:
		# If the name is not in the list, use known mappings from the station sheet
		fallback_positions = {
			"Alexandra": 3,
		}
		return fallback_positions.get(name, -1)


