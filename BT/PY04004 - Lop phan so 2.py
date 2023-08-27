from math import *

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutGon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
        return str(self.tu) + "/" + str(self.mau)
    
    def add(self, a):
        bcnn = self.mau * a.mau // gcd(self.mau, a.mau)
        self.tu = self.tu * bcnn // self.mau + a.tu * bcnn // a.mau
        self.mau = bcnn
        return self
    
tu1, mau1, tu2, mau2 = map(int, input().split())
a = PhanSo(tu1, mau1)
b = PhanSo(tu2, mau2)
a = a.add(b)
print(a.rutGon())