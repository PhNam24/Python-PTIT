base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

t = int(input())
while(t):
    s = input().upper()
    n = len(s) // 2
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += ord(s[i]) - 65
        sum2 += ord(s[i + n]) - 65
    ans = ""
    for i in range(n):
        tmp1 = ord(s[i]) - 65
        code1 = (tmp1 + sum1) % 26
        tmp2 = ord(s[i + n]) - 65
        code2 = (tmp2 + sum2) % 26
        code = (code1 + code2) % 26
        ans += base[code]
    print(ans)
    t -= 1