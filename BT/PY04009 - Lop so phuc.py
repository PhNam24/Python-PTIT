class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary < 0:
            return f'{self.real} - {abs(self.imaginary)}i'
        return f'{self.real} + {abs(self.imaginary)}i'

    def add(self, a):
        ans = Complex(0, 0)
        ans.real = self.real + a.real
        ans.imaginary = self.imaginary + a.imaginary
        return ans
    
    def multipy(self, a):
        ans = Complex(0, 0)
        ans.real = self.real * a.real - self.imaginary * a.imaginary
        ans.imaginary = self.real * a.imaginary + self.imaginary * a.real
        return ans    
    
t = int(input())
while t:
    r1, i1, r2, i2 = map(int, input().split())
    a = Complex(r1, i1)
    b = Complex(r2, i2)
    c = a.add(b)
    print(c.multipy(a), ', ' ,c.multipy(c), sep = "")
    t -= 1
