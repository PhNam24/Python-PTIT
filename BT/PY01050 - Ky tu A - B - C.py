def sinh(s, n, a, b, c):
    if len(s) == n and a > 0 and a <= b and b <= c:
        print(s)
    if len(s) < n:
        sinh(s + "A", n, a + 1, b, c)
        sinh(s + "B", n, a, b + 1, c)
        sinh(s + "C", n, a, b, c + 1)

n = int(input())
for i in range(3, n + 1):
    sinh("", i, 0, 0, 0)
