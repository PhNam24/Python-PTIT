t = int(input())
while(t):
    n, p = map(int, input().split())
    ans = 0
    for i in range(2, n + 1):
        if i % p == 0:
            while i % p == 0:
                i /= p
                ans += 1
    print(ans)
    t -= 1