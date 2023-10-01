import functools


class Student:
    def __init__(self, stt, name, point):
        self.code = "HS"
        if stt < 10:
            self.code += "0" + str(stt)
        else:
            self.code += str(stt)
        self.name = name
        self.sum = (point[0] + point[1]) * 2
        for i in range(2, 10):
            self.sum += point[i]
        self.sum /= 12
        if self.sum >= 9:
            self.rank = "XUAT SAC"
        elif self.sum >= 8:
            self.rank = "GIOI"
        elif self.sum >= 7:
            self.rank = "KHA"
        elif self.sum >= 5:
            self.rank = "TB"
        else:
            self.rank = "YEU"
        
        self.sum = round(self.sum, 5)
    
    def __str__(self) -> str:
        scale = pow(10, 1)
        return f'{self.code} {self.name} {round(self.sum * scale) / scale} {self.rank}'

def cmp(a, b):
    if a.sum != b.sum:
        if a.sum > b.sum:
            return -1
        else:
            return 1
    if a.code < b.code:
        return -1
    return 1

n = int(input())
a = []
for i in range(n):
    name = input()
    point = list(map(float, input().split()))
    a.append(Student(stt = i + 1, name = name, point = point))
a.sort(key = functools.cmp_to_key(cmp))
for i in a:
    print(i)