from tests import tests
from station1 import solution_station_1
from station2 import solution_station_2
from station3 import solution_station_3
from station4 import solution_station_4
from station5 import solution_station_5
from station6 import solution_station_6
from station7 import solution_station_7

# List three observations of all inputs (not sample inputs) observed at the same time
# Format: (time: str, station1_input: int, station2_input: str, station3_input: int, station4_input: int, station5_input: str, station6_input: int, station7_input: str)
# Example: ('12:30:00', 1, '1990-01-01', 2, 3, "John", 4, "e=mc^2")
observation1 = ('10:25:18',99, '2024-05-12', 39416, 3941, "Maciej", 39, "a+c+b")
observation2 = ('10:25:21',99, '2024-02-15', 78510, 7851, "Nadee", 78, "b+e")
observation3 = ('10:25:31',35, '2024-02-26', 44121, 4412, "Jelle", 44, "d+b+e")
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
#tests.Test_Exercise(combined_algorithm);