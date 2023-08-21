d = [0] * 42
tmp = 10
cnt = 0
while tmp != 0:
    a = list(map(int, input().split()))
    tmp -= len(a)
    for i in a:
        if d[i % 42] == 0:
            d[i % 42] = 1
            cnt += 1
print(cnt)