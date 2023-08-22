from math import *

def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

n = int(input())
a = list(map(int, input().split()))
d = [0] * int(1e6 + 5)
for i in a:
    if snt(i):
        d[i] += 1;
for i in range(len(a)):
    if d[a[i]] != 0:
        print(a[i], d[a[i]])
        d[a[i]] = 0


