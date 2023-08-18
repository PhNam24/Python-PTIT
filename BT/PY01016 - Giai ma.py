t = int(input())
while t:
    s = input()
    for i in range(len(s)):
        if s[i].isdigit():
            for j in range(int(s[i])): 
                print(s[i -1], end = "")
    print("\n")
    t -= 1