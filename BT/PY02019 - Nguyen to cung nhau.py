from math import *

n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
for i in range(n):
    for j in range(i + 1, n):
        if gcd(a[i], a[j]) == 1 and a[i] < a[j]:
            print(a[i], a[j])
