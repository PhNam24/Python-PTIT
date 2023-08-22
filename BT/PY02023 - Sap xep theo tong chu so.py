import functools

def cmp(s1, s2):
    sum1 = 0
    sum2 = 0
    for i in s1:
        sum1 += int(i)
    for i in s2:
        sum2 += int(i)
    if sum1 == sum2:
        if int(s1) < int(s2):
            return -1
        else:
            return 1
    elif sum1 < sum2:
        return -1
    return 1

t = int(input())
while t:
    n = int(input())
    a = list(input().split())
    a.sort(key = functools.cmp_to_key(cmp))
    for i in a:
        print(i, end = " ")
    print()
    t -= 1