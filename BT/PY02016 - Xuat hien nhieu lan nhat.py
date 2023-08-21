t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    d = [0] * int(1e6 + 5)
    cnt = -1e9
    m = -1e9
    for i in a:
        d[i] += 1
        cnt = max(cnt, d[i])
        m = max(m, i)
    if cnt > n / 2:
        for i in range(m + 1):
            if d[i] == cnt:
                print(i)
                break
    else:
        print("NO")
    t -= 1