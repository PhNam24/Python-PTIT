n, m = map(int, input().split())
a = []
b = [[0] * m] * n
for i in range(n):
    a.append(list(map(int, input().split())))
    
X = [-1, -1, -1, 0, 0, 1, 1, 1]
Y = [-1, 0, 1, -1, 1, -1, 0, 1]
print(b)
cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            b[i][j] = 1
            for k in range(8):
                i1 = i + X[k]
                j1 = j + Y[k]
                if  i1 >= 0 and i1 < n and j1 >= 0 and j1 < m and a[i1][j1] >= 0 and b[i1][j1] == 0:
                    cnt += a[i1][j1]
                    b[i1][j1] = 1
print(b)                
print(cnt) 