t = int(input())
while t:
    p, q = map(int, input().split())
    ip = input().split()
    if len(ip) == 1:
        x1 = ip[0]
        x2 = input()
    else:
        x1, x2 = ip
    tong = p + q
    p = min(p, q)
    q = tong - p
    tmp1, tmp2 = x1, x2
    x1 = x1.replace(str(q), str(p))
    x2 = x2.replace(str(q), str(p))
    tmp1 = tmp1.replace(str(p), str(q))
    tmp2 = tmp2.replace(str(p), str(q))
    print(min(int(x1) + int(x2), int(tmp1) + int(tmp2)), max(int(x1) + int(x2), int(tmp1) + int(tmp2)))
    t -= 1