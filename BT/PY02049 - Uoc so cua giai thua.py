t = int(input())
while(t):
    n, p = map(int, input().split())
    cnt = 0
    for i  in range(1, n + 1):
        if i % p == 0:
            while i % p == 0:
                i /= p
                cnt += 1
    print(cnt)
    t -= 1