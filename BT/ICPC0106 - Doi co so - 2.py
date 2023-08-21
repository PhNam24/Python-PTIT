from math import *

base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']

t = int(input())
while t:
    k = int(input())
    s = input()
    if k == 2:
        print(s)
    else:
        ans = ""
        a = int(log2(k))
        b = len(s) % a
        for i in range(len(s) - 1, b - 1, -a):
            tmp = 0
            for j in range(a):
                tmp += int(s[i - j]) * (2 ** j)
            ans = str(base[tmp]) + ans
        if b != 0:
            tmp = 0
            for i in range(b - 1, -1, -1):
                tmp += int(s[i]) * (2 ** (b - i - 1))
            ans = str(base[tmp]) + ans
        print(ans)
    t -= 1