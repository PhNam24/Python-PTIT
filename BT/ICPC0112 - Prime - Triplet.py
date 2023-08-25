snt = [0] * int(1e6 + 5)

snt[0] = 1
snt[1] = 1
for i in range(2, 1421):
    if snt[i] == 0:
        for j in range(i * i, int(1e6) + 5, i):
            snt[j] = 1;

t = int(input())
while t:
    n = int(input())
    cnt = 0
    for i in range(n - 5):
        if snt[i] == 0 and snt[i + 6] == 0:
            if snt[i + 2] == 0 or snt[i + 4] == 0:
                cnt += 1
    print(cnt)
    t -= 1