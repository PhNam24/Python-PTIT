t = int(input())
while t:
    s = input()
    s += '.'
    ans = int(1e9)
    tmp = 0
    for i in range(len(s)):
        if s[i].isdigit():
            tmp = tmp * 10 + int(s[i])
        elif i != 0 and s[i - 1].isdigit():
            ans = min(ans, tmp)
            tmp = 0
    print(ans)    
    t -= 1