33	32704
True	?
58	17371
False	
23	11744
False	
22	58547
False	
7	99991
False	

def solution_station_3(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
