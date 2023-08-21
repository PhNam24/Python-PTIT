t = int(input())
while t:
    s = input()
    n = input()
    cnt = 0
    idx = s.find(n)
    while idx != -1:
        cnt += 1
        idx = s.find(n, idx + len(n))
    print(cnt)
    t -= 1