t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    x, y, z = int(1e8), int(1e8), int(1e8)
    i = 0
    while i < len(a):
        if a[i] <= x:
            x, y, z = a[i], x, y
        elif a[i] <= y:
            y, z = a[i], y
        elif a[i] <= z:
            z = a[i]
        i += 1
    print(x + y + z)
    t -= 1