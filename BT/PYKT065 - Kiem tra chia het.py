from math import *

def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

while 1:
    s = input().split()
    if s[0] == '-1':
        break
    l, r = map(int, s)
    n = int(input())
    cnt = 0
    for i in range(l, r + 1):
        check = 0
        for j in range(2, n + 1):
            if i % j == 0:
                check = 1
                break
        if check == 1:
            continue
        else:
            cnt += 1
    print(cnt)