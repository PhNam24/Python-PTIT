s = input()
s = s[::-1]
ans = ""
d = 0
for i in s:
    if d % 3 == 0 and d != 0:
        ans += ',';
        d = 0
    ans += i
    d += 1
print(ans[::-1])