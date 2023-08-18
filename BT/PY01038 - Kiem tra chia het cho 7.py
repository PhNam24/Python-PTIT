t = int(input())
while t:
    n = int(input())
    d = 0
    while d <= 1000:
        if n % 7 == 0:
            print(n)
            break
        n += int(str(n)[::-1])
        d += 1
    if d > 1000: 
        print(-1)
    t -= 1