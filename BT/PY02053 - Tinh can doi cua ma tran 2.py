n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
k = int(input())
tren = 0
duoi = 0
for i in range(n):
    for j in range(n):
        if n - j - 1 < i:
            tren += a[i][j]
        elif n - j - 1 > i:
            duoi += a[i][j]
if(abs(tren - duoi) <= k):
    print("YES")
else:
    print("NO")
print(abs(tren - duoi))