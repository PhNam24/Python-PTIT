t = int(input())
while t:
    s = input()
    s += '.'
    d = {}
    for i in s:
        d[i] = 0
    for i in range(len(s) - 1):
        d[s[i]] += 1
        if s[i] != s[i + 1]:
            print(d[s[i]], s[i], sep = "", end = "")
            d[s[i]] = 0 
    print()
    t -= 1
