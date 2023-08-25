a = []

i = 1
while i <= int(1e18):
    j = 1
    while j <= int(1e18):
        k = 1
        while k <= int(1e18):
            a.append(i * j * k)
            k *= 5
        j *= 3
    i *= 2

a.sort()

def find(l, r, x):
    if l > r:
        return "Not in sequence"
    m = (l + r) // 2
    if a[m] == x:
        return m + 1
    if a[m] < x:
        return find(m + 1, r, x)
    return find(l, m - 1, x)

t = int(input())
while t:
    n = int(input())
    print(find(0, len(a), n))
    t -= 1