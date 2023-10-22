def check(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

def Pow(n, k, m):
    if(k == 1):
        return n
    if(k == 0):
        return 1
    tmp = Pow(n, k / 2, m)
    if(k % 2 != 0):
        return (((n * tmp) % m) * tmp) % m
    else:
        return (tmp * tmp) % m

t = int(input())
while t:
    n, m = map(int, input().split())
    s = input()
    if (len(s) > n):
        print(0)
    elif len(s) == n:
        print(1)
    else:
        cnt = n - len(s)
        if(check(s)):
            print(2 * pow(26, cnt, m) - 1)
        else:
            print(2 * pow(26, cnt, m))
    t -= 1