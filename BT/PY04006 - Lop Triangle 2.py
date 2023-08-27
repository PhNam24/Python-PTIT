from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, b):
        xx = self.x - b.x
        yy = self.y - b.y
        d = sqrt(xx * xx + yy * yy)
        return d


class Triangle:
    def __init__(self, p1, p2, p3):
        self.A = p1
        self.B = p2
        self.C = p3
    
    def perimeter(self):
        AB = self.A.distance(self.B)
        AC = self.A.distance(self.C)
        BC = self.B.distance(self.C)
        if max(AB, AC, BC) * 2 >= AB + AC + BC:
            return "INVALID"
        area = 0.25 * sqrt((AB + AC + BC) * (AB + AC - BC) * (AB - AC + BC) * (AC -  AB + BC))
        return f'{area:.2f}'
    
t = int(input())
a = []
for i in range(t):
    a += list(map(float, input().split()))

idx = 0
for i in range(t):
    triangle = Triangle(Point(a[idx], a[idx + 1]), Point(a[idx + 2], a[idx + 3]), Point(a[idx + 4], a[idx + 5]))
    print(triangle.perimeter())
    idx += 6
