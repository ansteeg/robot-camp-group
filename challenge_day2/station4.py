import numpy as np

def solution_station_4(n):
    if n < 2:
        return False
    if n == 2:   
        return True
    if n % 2 == 0:  
        return False
    
    for i in range(3, int(np.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

#print(solution_station_4(2))   # True
#print(solution_station_4(9))   # False
#print(solution_station_4(17))  # True
