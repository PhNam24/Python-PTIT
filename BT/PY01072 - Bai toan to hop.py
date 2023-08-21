n, k = map(int, input().split())

def Try(i, ans):
    if len(ans) == k:
        for i in ans:
            print(i, end = " ")
        print()
        return
    for j in range(i, len(a)):
        Try(j + 1, ans + [a[j]])

a = list(map(int, input().split()))
a = sorted(list(set(a)))

Try(0, [])
