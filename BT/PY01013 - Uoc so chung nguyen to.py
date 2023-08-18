from math import *

def snt(n):
    if n < 2: return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return 0
    return 1

def calc(n):
    if n < 10: return n
    t = 0
    while n:
        t += n % 10
        n //= 10
    return t

t = int(input())
while t:
    a, b = map(int, input().split())
    g = gcd(a, b)
    if snt(calc(g)): print("YES")
    else: print("NO") 
    t -= 1  