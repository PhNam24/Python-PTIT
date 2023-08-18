from math import *

n, k = map(int, input().split())
d = 0
for i in range(10**(k - 1), 10**k - 1):
    if gcd(i, n) == 1:
        print(i, end = " ")
        d += 1
    if d == 10:
        print("\n")
        d = 0