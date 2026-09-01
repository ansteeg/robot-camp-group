import math

def f(x):
    return math.sin(x)

# Voorbeelden
inputs = [0, 0.2, 2.6, 2.7, 1.6, 2.5]
for i in inputs:
    print(f"{i} : {f(i):.4f}")
