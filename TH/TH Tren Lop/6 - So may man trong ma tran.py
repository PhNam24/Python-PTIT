n, m = map(int, input().split())
a = []
Max = int(-1e9)
Min = int(1e9)
for i in range(n):
    tmp = list(map(int, input().split()))
    Min = min(Min, min(tmp))
    Max = max(Max, max(tmp))
    a.append(tmp)
    
ans = Max - Min
cnt = 0
res = []
for i in range(n):
    for j in range(m):
        if a[i][j] == ans:
            res.append(f"Vi tri [{i}][{j}]")
            cnt += 1
if cnt == 0:
    print("NOT FOUND")
else:
    print(ans)
    for i in res:
        print(i)