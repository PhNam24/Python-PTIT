from math import *

def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def check(s):
    if(snt(int(s)) == 0 or snt(int(s[::-1]))) == 0:
        return "No"
    sum = 0
    for i in s:
        if snt(int(i)) == 0:
            return "No"
        sum += int(i)
    if snt(sum) == 0:
        return "No"
    return "Yes"
    

t = int(input())
while t:
    print(check(input()))
    t -= 1