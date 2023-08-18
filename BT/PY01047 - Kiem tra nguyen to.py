from math import *

def snt(n):
    if n < 2:
        return "NO"
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return "NO"
    return "YES"

t = int(input())
while t:
    s = input()
    print(snt(int(s[len(s) - 4::])))
    t -= 1