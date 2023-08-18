t = int(input())
while t:
    n = float(input())
    sum = 0
    if n % 2:
        for i in range(1, int(n) + 1, 2):
            sum += 1 / i
    else:
        for i in range(2, int(n) + 2, 2):
            sum += 1 / i
    print(f'{sum:.6f}')
    t -= 1