from math import *

def Pow(a, b):
    if b == pow(2, a - 1):
        return a
    elif b > pow(2, a - 1):
        return Pow(a - 1, b - pow(2, a - 1))
    return Pow(a - 1, b)

t = int(input())
while(t):
    n, k = map(int, input().split())
    if k % 2 == 1:
        print("A")
    else:
        print(chr(Pow(n, k) + 65 - 1))
    t -= 1