from math import *

def snt(n):
    n = int(n)
    if n < 2: return 0
    for i in range(2, n):
        if n % i == 0: return 0
    return 1

t = int(input())

while t:
    n = int(input())
    cnt = 0
    for i in range(n):
        if gcd(i, n) == 1: cnt += 1
    if(snt(cnt)): print("YES")
    else: print("NO")
    t -= 1