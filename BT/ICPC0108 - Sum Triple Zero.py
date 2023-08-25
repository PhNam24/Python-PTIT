t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
            if a[i] + a[left] + a[right] == 0:
                left += 1
                cnt += 1
            elif a[i] + a[left] + a[right] > 0:
                right -= 1
            else:
                left += 1
    print(cnt)
    t -= 1