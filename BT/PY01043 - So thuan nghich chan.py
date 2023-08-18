def check(s):
    for i in s:
        if int(i) % 2: 
            return 0;
    return 1

arr = []
m = 2
while m <= 888:
    if check(str(m)):
        arr.append(int(str(m) + str(m)[::-1]))
    m += 2
t = int(input())
while t:
    n = int(input())
    for i in arr:
        if i >= n: 
            break
        print(i, end = " ")
    print("\n") 
    t -= 1