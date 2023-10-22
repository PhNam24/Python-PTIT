t = int(input())
while t:
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = list(map(float, input().split()))
        a.append(tmp[0])
        b.append(tmp[1])
    cnt = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and b[i] < b[j]:
                cnt[i] = max(cnt[i], cnt[j] + 1)
    print(max(cnt))
    t -= 1