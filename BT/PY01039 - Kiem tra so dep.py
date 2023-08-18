def check(s):
    ss = set(list(s))
    if len(ss) > 2:
        return "NO"
    for i in range(2, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[1]) - ord(s[0])):
            return "NO"
    return "YES"

t = int(input())
while t:
    s = input()
    print(check(s))
    t -= 1