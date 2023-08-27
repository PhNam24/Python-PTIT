n = int(input())
a = []

while 1:
    a += list(map(int, input().split()))
    if len(a) == n:
        break
    
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