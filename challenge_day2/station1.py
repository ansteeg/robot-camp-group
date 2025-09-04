# Madeleine and Kacper

def solution_station_1(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

print(solution_station_1(69))


print(solution_station_1(4))