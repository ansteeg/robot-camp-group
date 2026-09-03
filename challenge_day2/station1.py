def solution_station_1(n):

    if n < 0:
        print("Please enter a non-negative number.")
        return
    if n == 0:
        print("0 is the 0th Fibonacci number")
        return
    if n == 1:
        print("1 is the 1st Fibonacci number")
        return

    a = 0
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

###    print(f"{n} is {b} in the Fibonacci sequence")
    return b