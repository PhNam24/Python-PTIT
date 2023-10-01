file = open("D:\Code\CodePTIT\Python-PTIT\TH\TH2\DATA.in", "r")

def check(s):
    if len(s) > 9:
        return 0
    for i in s:
        if not str(i).isdigit():
            return 0
    if int(s) > 2 ** 31 - 1:
        return 0
    elif int(s) < -(2 ** 31):
        return 0
    return 1

a = []
for i in file:
    tmp = i.strip().split()
    for j in tmp:
        if(check(j) == 0):
            a.append(j)
a.sort()
for i in a:
    print(i, end = " ")