def solution_station_1(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return solution_station_1(n-1) + solutions_station_1(n-2)

print (solution_station_1(69))
  
# italian mathematician (fibonacci sequence)
# 0 0
# 69 ?
# 30 832040
# 16 987
# 20 6765
# 62 4052739537881
# 38 39088169
