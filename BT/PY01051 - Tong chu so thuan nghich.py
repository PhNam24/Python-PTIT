def check(s):
    n = 0
    for i in s:
        n += int(i)
    if n < 10:
        return "NO"
    if str(n) != str(n)[::-1]:
        return "NO"
    return "YES"

t = int(input())
while t:
    print(check(input()))
    t -= 1