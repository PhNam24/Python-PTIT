def check(s):
    if len(s) % 2 == 0:
        return "NO";
    for i in range(0, len(s) - 2, 2):
        if s[i] != s[i + 2]:
            return "NO"
    return "YES"

t = int(input())
while t:
    print(check(input()))
    t -= 1