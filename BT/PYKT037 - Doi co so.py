base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

t = int(input())
while t:
    n, b = map(int, input().split())
    ans = ""
    while n:
        ans += base[n % b]
        n //= b
    print(ans[::-1])
    t -= 1