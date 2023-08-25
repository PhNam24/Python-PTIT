n = int(input())
a = list(map(int, input().split()))
chan = []
le = []
for i in range(n):
    if a[i] % 2 == 1:
        le.append(a[i])
    else:
        chan.append(a[i])

chan.sort(reverse=True)
le.sort()

for i in range(n):
    if a[i] % 2 == 1:
        print(le[-1], end = " ")
        le.pop()
    else:
        print(chan[-1], end = " ")
        chan.pop()