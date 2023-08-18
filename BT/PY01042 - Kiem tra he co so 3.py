def check(s):
    for i in s:
        if i != '0' and i != '1' and i != '2':
            return "NO"
    return "YES"

t = int(input())
while t:
    s = input()
    print(check(s))
    t -= 1