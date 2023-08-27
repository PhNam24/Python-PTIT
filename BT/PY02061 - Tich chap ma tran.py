t = int(input())
while t:
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    b = []
    for i in range(3):
        b.append(list(map(int, input().split())))
    sum = 0
    for i in range(n - 2):
        for j in range(m - 2):
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    sum += a[k][l] * b[k - i][l - j]
    print(sum)
    t -= 1