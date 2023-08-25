seive = [0] * int(31630)
seive[0] = 1
seive[1] = 1
for i in range(2, 364):
    if seive[i] == 0:
        for j in range(i * i, 31630, i):
            if seive[j] == 0:
                seive[j] = 1

snt = []
for i in range(2, 31630):
    if seive[i] == 0:
        snt.append(i * i)
        
n = int(input())
cnt = 0
for i in range(len(snt)):
    if snt[i] > n:
        break
    if snt[i] ** 4 <= n:
        cnt += 1
    for j in range(i + 1, len(snt)):
        if snt[i] * snt[j] <= n:
            cnt += 1
        else:
            break
print(cnt)
