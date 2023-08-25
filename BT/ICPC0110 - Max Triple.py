t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    x, y, z = int(-1e8), int(-1e8), int(-1e8)
    for i in a:
        if i >= x:
            x, y, z = i, x, y
        elif i >= y:
            y, z = i, y
        elif i >= z:
            z = i
    print(x + y + z)
    t -= 1