p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while 1:
    ss = input()
    if ss[0] == '0':
        break
    k, s = ss.split()
    k = int(k)
    ans = ""
    for i in s:
        ans += p[(p.find(i) + k) % 28]
    print(ans[::-1])
