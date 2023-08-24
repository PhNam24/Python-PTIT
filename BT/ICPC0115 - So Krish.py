from math import *

def check(s):
    sum = 0
    for i in s:
        sum += factorial(int(i))
    if sum != int(s):
        return "No"
    return "Yes"
    

t = int(input())
while t:
    print(check(input()))
    t -= 1