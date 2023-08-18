t = int(input())
while t:
    arr = list(map(float, input().split()))
    cnt = 0
    while(arr[0] < arr[2]):
        arr[0] = arr[0] + arr[0] * arr[1] / 100
        cnt += 1
    print(cnt)
    t -= 1