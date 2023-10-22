t = int(input())
while t:
    n, m, k = map(int, input().split())
    a = [[0] * (m + 1)]
    for i in range(n): 
        a.append([0] + list(map(int, input().split())))
    for i in range(1, n + 1):
        for j in range(1, m + 1): 
            a[i][j] += a[i - 1][j]
    ans = []
    for i in range(1, n-k+2):
        tmp, s = [], 0
        for j in range(1, k + 1): s += a[i + k - 1][j] - a[i - 1][j]
        tmp.append(s)
        for j in range(2, m-k+2):
            s = s + (a[i + k - 1][j + k - 1] - a[i - 1][j + k - 1]) - (a[i + k - 1][j - 1] - a[i - 1][j - 1])
            tmp.append(s)
        ans.append(tmp)
    k*=k
    for i in ans: 
        for j in i: print(j // k, end=' ')
        print()
    t -= 1