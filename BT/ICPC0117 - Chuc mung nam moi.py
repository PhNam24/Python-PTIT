from math import *

t = int(input())
ans = []
while t:
    ans.append(input())
    t -= 1
print(len(set(ans)))