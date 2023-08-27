from math import *
from decimal import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(a, b):
        xx = a.x - b.x
        yy = a.y - b.y
        d = sqrt(xx ** 2 + yy ** 2)
        return f'{d:.4f}'


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1