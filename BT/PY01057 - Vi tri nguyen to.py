from math import *

def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def check(s):
    for i in range(len(s)):
        if (snt(i) and snt(int(s[i])) == 0) or (snt(i) == 0 and snt(int(s[i]))):
            return "NO"
    return "YES"

t = int(input())
while t:
    print(check(input()))
    t -= 1