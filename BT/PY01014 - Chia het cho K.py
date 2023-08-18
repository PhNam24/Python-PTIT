a, k, n = map(int, input().split())

m = k - (a % k)

arr = []

while m <= n - a:
    arr.append(m)
    m += k;
if len(arr): 
    for i in arr:
        print(i, end = " ")
else: print(-1)