while 1:
    a = list(map(int, input().split()))
    if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0:
        break
    cnt = 0
    while a.count(a[0]) != 4:
        tmp = a.copy()
        for i in range(3):
            a[i] = abs(tmp[i] - tmp[i + 1])
        a[3] = abs(tmp[3] - tmp[0])
        cnt += 1
    print(cnt)