t = int(input())
while t:
    s = input()
    sum = 0
    product = 1
    cnt = 0
    le = 0
    for i in range(len(s)):
        if i % 2 == 0:
            sum += int(s[i])
        else:
            le += 1
            if s[i] == '0':
                cnt += 1
                continue
            else:
                product *= int(s[i])
    if cnt == le:
        product = 0
    print(sum, product)
    t -= 1