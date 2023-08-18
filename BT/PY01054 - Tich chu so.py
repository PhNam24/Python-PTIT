t = int(input())
while t:
    s = input()
    n = 1
    for i in s:
        if i != '0':
            n *= int(i)
    print(n)
    t -= 1