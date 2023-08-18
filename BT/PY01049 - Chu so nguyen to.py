from math import *

def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def check(s):
    if snt(len(s)) != 1:
        return "NO"
    cnt = 0
    for i in s:
        if snt(int(i)):
            cnt += 1
    if cnt <= len(s) - cnt:
        return "NO"
    return "YES"

t = int(input())
while t:
    print(check(input()))
    t -= 1