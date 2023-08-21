def check(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return "NO"
    return "YES"

t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = sorted(a)
    b = sorted(b)
    print(check(a, b))
    t -= 1