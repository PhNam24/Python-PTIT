from math import *

t = int(input())
while t:
    n = int(input())
    print(1, end = " ")
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n /= i
                cnt += 1
            print("* ", i, "^", cnt, sep = "", end = " ")
    if(n > 1): print(" * ", n ,"^1", sep = "", end = " ")
    print("\n")
    t -= 1