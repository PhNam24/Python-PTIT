n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    a[i] = [a[i], b[i]]
a.sort(key=lambda x: x[0] - x[1])
cnt = 0
for i in range(k): 
    cnt += a[i][0]
for i in range(k, n):
    if a[i][0] < a[i][1]:
        cnt += a[i][0]
        k += 1
for j in range(k, n): 
    cnt += a[j][1]
print(cnt)