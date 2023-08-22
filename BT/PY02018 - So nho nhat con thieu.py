n = int(input())
a = list(map(int, input().split()))
d = [0] * 30005
m = int(-1e9)
for i in a:
    d[i] += 1
    m = max(m, i)
for i in range(1, n + 2):
    if d[i] == 0:
        print(i)
        break
