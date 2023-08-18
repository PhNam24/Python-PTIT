def check(s):
    for i in s:
        if i != '4' and i != '7': return 0
    return 1

t = int(input())
while t:
    n = input()
    if(check(n)): print("YES")
    else: print("NO")
    t -= 1