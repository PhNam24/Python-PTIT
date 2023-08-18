def sol(n, a, b, c):
    if n == 1:
        print(a, "->", c)
        return
    sol(n - 1, a, c, b)
    sol(1, a, b, c)
    sol(n - 1, b, a, c)

n = int(input())
sol(n, 'A', 'B', 'C')