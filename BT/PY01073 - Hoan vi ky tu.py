s = input()
n = len(s)
mark = [0] * n

def Try(ans):
    if len(ans) == n:
        print(ans)
        return
    for i in range(n):
        if mark[i] == 0:
            mark[i] = 1
            Try(ans + s[i])
            mark[i] = 0

Try("")