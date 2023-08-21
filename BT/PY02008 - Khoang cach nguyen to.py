from math import *

snt = []
snt = [1] * int(2e6 + 5)
snt[0] = 0
snt[1] = 0
for i in range(2, int(sqrt(len(snt))) + 1):
    if snt[i] == 1:
        for j in range(i * i, len(snt), i):
            if snt[j] == 1:
                snt[j] = 0

a = []
for i in range(len(snt)):
    if snt[i] == 1:
        a.append(i)

n, x = map(int, input().split())
ans = []
ans.append(x)
for i in range(1, n + 1):
    ans.append(ans[i - 1] + a[i - 1])
    
for i in ans:
    print(i, end = " ")