def check(s):
    if len(s) < 3:
        return "NO"
    tang = []
    giam = []
    tang.append(1)
    giam.append(1)
    for i in range(1, len(s)):
        if s[i] > s[i - 1]: 
            tang.append(tang[i - 1] + 1)
        else:
            tang.append(1)
        giam.append(1)
    for i in range(len(s) - 2, -1, -1):
        if s[i] > s[i + 1]:
            giam[i] = giam[i + 1] + 1
        else:
            giam[i] = 1
    for i in range(len(s)):
        if tang[i] + giam[i] - 1 == len(s):
            return "YES"
    return "NO"
t = int(input())
while t:
    s = input()
    print(check(s))
    t -= 1