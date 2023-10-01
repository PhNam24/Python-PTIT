import functools

class Student:
    def __init__(self, stt, name, point, dtoc, kv):
        self.code = "TS"
        if stt < 10:
            self.code += "0" + str(stt)
        else:
            self.code += str(stt)
        self.name = name
        self.point = point
        self.dtoc = dtoc
        self.kv = kv
        if self.dtoc == "Kinh":
            self.extra = 0
        else:
            self.extra = 1.5
        if kv == 1:
            self.extra += 1.5
        elif kv == 2:
            self.extra += 1
        else:
            self.extra += 0
        self.tong = self.point + self.extra
        if self.tong >= 20.5:
            self.status = "Do"
        else:
            self.status = "Truot"
    
    def __str__(self):
        return self.code + " " + self.name + " " + f'{self.tong:.1f}' + " " + self.status
    
def cmp(a, b):
    if a.tong != b.tong:
        if a.tong > b.tong:
            return -1
        else:
            return 1
    return a.code < b.code

def normalization(name):
    name = str(name).lower().split()
    ans = ""
    for i in range(len(name)):
        ans += name[i][0].upper() + name[i][1:]
        if i < len(name) - 1:
            ans += " "
    return ans
        
    

n = int(input())
a = []

for i in range(n):
    name = input().strip()
    name = normalization(name)
    point = float(input())
    dtoc = input()
    kv = int(input())   
    a.append(Student(stt = i + 1, name = name, point = point, dtoc=dtoc, kv = kv))

a.sort(key=functools.cmp_to_key(cmp))

for i in a:
    print(i)