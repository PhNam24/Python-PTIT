n = int(input());
a = list(map(int, input().split()))
idx = 1
while idx < len(a):
    if (a[idx] + a[idx - 1]) % 2 == 0:
        a.pop(idx)
        a.pop(idx - 1)
        if idx > 1:
            idx -= 1
    else:
        idx += 1
print(len(a))