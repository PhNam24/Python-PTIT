import functools

def cmp(s1, s2):
    product1 = 1
    product2 = 1
    for i in s1:
        product1 *= int(i)
    for i in s2:
        product2 *= int(i)
    if product1 == product2:
        if int(s1) < int(s2):
            return -1
        else:
            return 1
    elif product1 < product2:
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