def calc(a, n, idx):
    l = 0
    r = n - 1
    if idx != 0 and idx != n - 1:
        while True:
            if r != idx:
                if a[r] <= a[idx]:
                    return 0
                else:
                    r -= 1
            if l != idx:
                if a[l] > a[idx]:
                    return 0
                else:
                    l += 1
            if l == idx and r == idx:
                break
    elif idx == 0:
        for i in range(1, n):
            if a[i] <= a[idx]:
                return 0
    else:
        for i in range(n - 1):
            if a[i] > a[idx]:
                return 0
    return 1

t = int(input())
while(t):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        cnt += calc(a, n, i)
    print(cnt)
    t -= 1