from math import *

def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def check(n):
    if snt(n) == 0:
        return 0
    elif int(str(n)[::-1]) == n:
        return 0
    elif snt(int(str(n)[::-1])) == 0:
        return 0
    return 1



t = int(input())
while t:
    n = int(input())
    d = [0] * int(1e6 + 5)
    for i in range(13, n):
        if check(i):
            if int(str(i)[::-1]) < n:
                if d[i] != 1 and d[int(str(i)[::-1])] != 1:
                    print(i, str(i)[::-1], end = " ")
                    d[i] += 1
                    d[int(str(i)[::-1])] += 1

    print()
    t -= 1
