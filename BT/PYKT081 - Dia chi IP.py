def check(s):
    s = s.split('.')
    if len(s) < 4:
        return "NO"
    for i in s:
        if i.isdigit():
            if int(i) > 255 or int(i) < 0:
                return "NO"
        else:
            return "NO"
    return "YES"

t = int(input())
while t:
    print(check(input()))
    t -= 1