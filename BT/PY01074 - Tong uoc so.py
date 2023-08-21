snt = [1] * int(2e6 + 5)
snt[0] = 0
snt[1] = 0
for i in range(2, 1421):
    if snt[i] == 1:
        for j in range(i * i, len(snt), i):
            if snt[j] == 1:
                snt[j] = i

for i in range(2, len(snt)):
    if snt[i] == 1:
        snt[i] = i

ans = 0
t = int(input())
while t:
    n = int(input())
    while n > 1:
        ans += snt[n]
        n //= snt[n]
    t -= 1
print(ans)