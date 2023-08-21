t = int(input())
while t:
    n = int(input())
    d = [0] * 1001
    m = int(-1e9)
    for i in range(n):
        tmp = int(input())
        d[tmp] += 1
        m = max(m, d[tmp])
    for i in range(len(d)):
        if d[i] == m:
            print(i)
            break
    t -= 1