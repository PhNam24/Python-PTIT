from math import *

def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def check(s):
    n = 0
    for i in s:
        n += int(i)
    if snt(n):
        return "YES"
    return "NO"

t = int(input())
while t:
    print(check(input()))
    t -= 1