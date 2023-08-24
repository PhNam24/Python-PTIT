from math import *

def check(s):
    if s[0] != s[-1]:
        return "NO"
    return "YES"
    

t = int(input())
while t:
    print(check(input()))
    t -= 1