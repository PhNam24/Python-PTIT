import functools

class Customer:
    def __init__(self, stt, name, soNuoc):
        self.code = "KH"
        if stt < 10:
            self.code += "0" + str(stt)
        else:
            self.code += str(stt)
        self.name = name
        self.soNuoc = soNuoc
        if self.soNuoc <= 50:
            self.donGia = 100
            self.thue = 0.02
        elif self.soNuoc <= 100:
            self.donGia = 150
            self.thue = 0.03
        else:
            self.donGia = 200
            self.thue = 0.05
        self.tien = self.soNuoc * self.donGia * (1 + self.thue)
        
    def __str__(self):
        return f"{self.code} {self.name} {round(self.tien)}"
  
def cmp(a, b):
    return b.tien - a.tien
  
n = int(input())
a = []
for i in range(n):
    name = input()
    cu = int(input())
    moi = int(input())
    a.append(Customer(i + 1, name, moi - cu))
a.sort(key=functools.cmp_to_key(cmp))

for i in a:
    print(i)    
