fibo = []
fibo.append(0)
fibo.append(1)
fibo.append(1)
for i in range(3, 95):
    fibo.append(fibo[i - 1] + fibo[i - 2])

t = int(input())
while t:
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print(fibo[i], end = " ")
    print("\n")
    t -= 1