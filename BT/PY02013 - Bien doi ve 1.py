while 1:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(1)
        continue
    cnt = 1
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        cnt += 1
    print(cnt)
    