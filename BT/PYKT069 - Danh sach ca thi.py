import functools

class PhongThi:
    def __init__(self, code, date, time, roomID):
        self.code = "C"
        tmp = 3 - len(code)
        for i in range(tmp):
            self.code += "0"
        self.code += code
        self.date = date
        self.time = time
        self.roomID = roomID
        
    def __str__(self) -> str:
        return self.code + " " + self.date + " " + self.time + " " + self.roomID
    
def cmp(a, b):
    if a.date != b.date:
        if a.date < b.date:
            return -1
    elif a.time != b.time:
        if a.time < b.time:
            return -1
    if a.code < b.code:
        return -1
    return 1

file = open("D:\Code\CodePTIT\Python-PTIT\BT\InputFile\CATHI.in", "r")

n = int(file.readline())

a = []

for i in range(n):
    date = file.readline().strip()
    time = file.readline().strip()
    roomID = file.readline().strip()
    a.append(PhongThi(code = str(i + 1), date = date, time = time, roomID = roomID))

a.sort(key = functools.cmp_to_key(cmp))
for i in range(len(a)):
    print(a[i])