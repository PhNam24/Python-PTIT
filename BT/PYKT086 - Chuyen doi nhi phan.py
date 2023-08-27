from math import *

base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']

f = open("D:\CodePTIT\Python-PTIT\BT\DATA.in")

t = int(f.readline())
while t:
    k = int(f.readline())
    s = f.readline()
    s1 = ""
    for i in s:
        if i == '0' or i == '1':
            s1 += i
    if k == 2:
        print(s1)
    else:
        ans = ""
        a = int(log2(k))
        b = len(s1) % a
        for i in range(len(s1) - 1, b - 1, -a):
            tmp = 0
            for j in range(a):
                tmp += int(s1[i - j]) * (2 ** j)
            ans = str(base[tmp]) + ans
        if b != 0:
            tmp = 0
            for i in range(b - 1, -1, -1):
                tmp += int(s1[i]) * (2 ** (b - i - 1))
            ans = str(base[tmp]) + ans
        print(ans)
    t -= 1