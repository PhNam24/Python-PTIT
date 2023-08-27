class Student:
    def __init__(self, name, birth, p1, p2, p3):
        self.name = name
        self.birth = birth
        self.p1 = p1 
        self.p2 = p2
        self.p3 = p3
        self.sum = p1 + p2 + p3

    def __str__(self) -> str:
        return f'{self.name} {self.birth} {self.sum:.1f}'
    
    def normalization(self):
        s = self.birth.split("/")
        self.birth = ""
        for i in range(len(s) - 1):
            if len(s[i]) < 2:
                s[i] = "0" + s[i]
            self.birth += s[i] + "/"
        self.birth += s[2]
        return self.birth
        

name = input()
birth = input()
p1 = float(input())
p2 = float(input())
p3 = float(input())

student = Student(name, birth, p1, p2, p3)
student.normalization()
print(student)