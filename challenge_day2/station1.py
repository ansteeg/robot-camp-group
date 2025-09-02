# station1.py

def solution_station_1(n: int) -> int:
    
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")

    a, b = 0, 1   # F(0), F(1)
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    # Quick self-check
    print(solution_station_1(44))  # 701408733
