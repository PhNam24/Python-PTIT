t = int(input())
while t:
    s = input()
    if s[len(s) - 2] + s[len(s) - 1] == '86': 
        print("YES")
    else: print("NO")
    t -= 1