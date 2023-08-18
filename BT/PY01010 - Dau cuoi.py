t = int(input())

while t:
    s = input();
    if s[0] + s[1] == s[len(s) - 2] + s[len(s) - 1]: print("YES")
    else: print("NO")
    t -= 1