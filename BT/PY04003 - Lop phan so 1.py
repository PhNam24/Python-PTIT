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
    
tu, mau = map(int, input().split())
a = PhanSo(tu, mau)
print(a.rutGon())