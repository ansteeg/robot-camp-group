from tests import tests
from station1 import solution_station_1
from station2 import solution_station_2
from station3 import solution_station_3
from station4 import solution_station_4
from station5 import solution_station_5
from station6 import solution_station_6
from station7 import solution_station_7

# Observations aligned with tests' format
observation1 = ('13:37:12', 15, '2023-03-29', 86, 1837, 'Bassant', 17799, 'b*d+c+a')
observation2 = ('13:40:20', 25, '2024-06-20', 58972, 5387, 'Tibbe', 53, 'd+c')
observation3 = ('13:41:20', 55, '2024-05-17', 18374, 1837, 'Kian', 18, 'd+a*d+c')

# Format: (time: str, station1_input: int, station2_input: str, station3_input: int, station4_input: int, station5_input: str, station6_input: int, station7_input: str)
# 86461*84009*19498

def combined_algorithm(observations: tuple) -> int:
	output1 = solution_station_1(observations[1])
	output2 = solution_station_2(observations[2])
	output3 = solution_station_3(observations[3])
	output4 = solution_station_4(observations[4])
	output5 = solution_station_5(observations[5])
	output6 = solution_station_6(observations[6])
	output7 = solution_station_7(observations[7])
	assert isinstance(output1, int)
	assert isinstance(output2, str)
	assert isinstance(output3, bool)
	assert isinstance(output4, bool)
	assert isinstance(output5, int)
	assert isinstance(output6, float)
	assert isinstance(output7, float)
	return output1 * int.from_bytes(output2[0].encode("unicode_escape"), byteorder='big') * (3 if output3 else 2) * (5 if output4 else 4) * output5 * output6 * output7


FINAL_OUTPUT1 = combined_algorithm(observation1)
FINAL_OUTPUT2 = combined_algorithm(observation2)
FINAL_OUTPUT3 = combined_algorithm(observation3)

print(FINAL_OUTPUT1)
print(FINAL_OUTPUT2)
print(FINAL_OUTPUT3)

tests.Test_Exercise(combined_algorithm)


