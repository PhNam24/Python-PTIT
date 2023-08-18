from math import *

t = int(input())
while t:
    n = input()
    if gcd(int(n), int(n[::-1])) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1