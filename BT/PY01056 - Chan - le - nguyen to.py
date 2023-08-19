from math import *

def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def check(s):
    sum = 0;
    for i in range(len(s)):
        if i % 2 == 0:
            if int(s[i]) % 2 != 0:
                return "NO"
        else:
            if int(s[i]) % 2 == 0:
                return "NO"
        sum += int(s[i])
    if snt(sum):
        return "YES"
    return "NO"

t = int(input())
while t:
    print(check(input()))
    t -= 1