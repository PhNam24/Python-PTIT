class Rectangle:
    def __init__(self, length, width, Color):
        self.length = length
        self.width = width
        self.Color = Color.title()

    def check(self):
        if self.length <= 0 or self.width <= 0:
            return 0
        return 1

    def perimeter(self):
        if self.check() == 0:
            return "INVALID"
        return (self.length + self.width) * 2
    
    def area(self):
        if self.check():
            return self.length * self.width
        return ""

    def color(self):
        if self.check():
            return self.Color
        return ""
    
arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))