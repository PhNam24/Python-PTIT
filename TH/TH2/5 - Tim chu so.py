from math import *

t = int(input())
d = 1
while(t):
    print(f"Case #{d}: ", end = "")
    n = int(input())
    sqrt5 = sqrt(5)
    phi = (1 + sqrt5) / 2
    result = (phi ** n) / sqrt5
    ans = str(int(result))[:3]
    print(result)
    d += 1
    t -= 1