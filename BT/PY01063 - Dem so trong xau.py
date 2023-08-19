t = int(input())
while t:
    s = input()
    n = input()
    cnt = 0
    idx = 0
    while idx <= len(s):
        if s.find(n, idx):
            cnt += 1
            idx += s.find(n, idx) + len(n)
            print(s.find(n, idx))  
    print(cnt)
    t -= 1