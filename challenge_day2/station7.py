def solution_station_7(expression):
  locals_dict = {'a': 3, 'b': -1, 'c': 4, 'd': 7, 'e': 0.5}
  globals_dict = {"__builtins__": None}
  result = eval(expression, globals = globals_dict, locals = locals_dict)
  result = float(result)
  return result


  """ 
  hint: eval()
  e*a*d = 10.5
  d+c = 11
  b*a = -3
  e*b*d*a = -10.5
  e+b = -0.5
  e+d+a+b = 9.5
  a+d+b+c = 13
  a*d+e+b = 20.5
  e*b+d = 6.5

  a = 3
  b = -1
  c = 4
  d = 7
  e = 0.5
  """
  
