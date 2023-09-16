import functools

class CaThi:
    def __init__(self, code, date, time, id):
        self.code = "C"
        tmp = 3 - len(code)
        for i in range(tmp):
            self.code += "0"
        self.code += code
        self.date = date
        self.time = time
        self.id = id
    
    def __str__(self):
        return self.code + " " + self.date + " " + self.time + " " + self.id
    
def cmp(a, b):
    if a.date != b.date:
        if a.date > b.date:
            return 1
        else:
            return -1
    elif a.time != b.time:
        if a.time > b.time:
            return 1
        else:
            return -1
    if a.code > b.code:
        return 1
    return -1

file = open("D:\Code\CodePTIT\Python-PTIT\TH\TH1\CATHI.in", "r")

n = int(file.readline())

ans = []

for i in range(n):
    date = file.readline().strip()
    time = file.readline().strip()
    id = file.readline().strip()
    ans.append(CaThi(code = str(i + 1), date = date, time = time, id = id))
    
ans.sort(key = functools.cmp_to_key(cmp))

for i in ans:
    print(i)
    