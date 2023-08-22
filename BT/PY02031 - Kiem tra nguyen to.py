snt = [1] * 1005
snt[0] = 0 
snt[1] = 0
for i in range(2, 32):
    if snt[i] == 1:
        for j in range(i * i, 1005, i):
            snt[j] = 0

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(len(a)):
    for j in range(len(a[i])):
        print(snt[a[i][j]], end = " ")
    print()
