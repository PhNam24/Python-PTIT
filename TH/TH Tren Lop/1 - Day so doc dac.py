t = int(input())

def check(a, n):
    d = {}
    if a.count(a[0]) == n:
        return "NO"
    for i in a:
        d[i] = 0
    for i in range(1, n):
        if a[i] == a[i - 1]:
            return "NO"
        d[a[i]] = d[a[i]] + 1
    for i in range(3, n):
        if a[i] == a[i - 2] and a[i - 1] == a[i - 3]:
            return "NO" 
    for i in d:
        if d[i] == 1:
            return "YES"
    return "NO"

while(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(check(a, n))  
    t -= 1