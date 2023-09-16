a, b, m = map(int, input().split())
cnt = 0
l = []
for i in range(a, b + 1):
    tmp = bin(i)[2:]
    if tmp == tmp[::-1]:
        cnt += 1
print(cnt)
print(bin(17))