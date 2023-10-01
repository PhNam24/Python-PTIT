class NhanVien:
    def __init__(self, code, name, room, luong, ngayCong) -> None:
        self.code = code
        self.name = name
        self.room = room
        self.luong = luong
        self.ngayCong = ngayCong
        year = int(self.code[1:3])
        if year <= 3:
            if self.code[0] == 'A':
                self.heSo = 10
            elif self.code[0] == 'B':
                self.heSo = 10
            elif self.code[0] == 'C':
                self.heSo = 9  
            elif self.code[0] == 'D':
                self.heSo = 8 
        elif year <= 8:
            if self.code[0] == 'A':
                self.heSo = 12
            elif self.code[0] == 'B':
                self.heSo = 11
            elif self.code[0] == 'C':
                self.heSo = 10  
            elif self.code[0] == 'D':
                self.heSo = 9 
        elif year <= 15:
            if self.code[0] == 'A':
                self.heSo = 14
            elif self.code[0] == 'B':
                self.heSo = 13
            elif self.code[0] == 'C':
                self.heSo = 12  
            elif self.code[0] == 'D':
                self.heSo = 11   
        else:
            if self.code[0] == 'A':
                self.heSo = 20
            elif self.code[0] == 'B':
                self.heSo = 16
            elif self.code[0] == 'C':
                self.heSo = 14  
            elif self.code[0] == 'D':
                self.heSo = 13 
        self.tong = self.luong * self.ngayCong * self.heSo * 1000
        
    def __str__(self):
        return str(self.code) + " " + str(self.name) + " " + str(self.room) + " " + str(self.tong)
        
n = int(input())
map = {}
for i in range(n):
    tmp = input().split()
    code = tmp[0]
    room = ""
    for i in range(1, len(tmp)):
        room += tmp[i]
        if i < len(tmp) - 1:
            room += " "
    map[code] = room

a = []

n = int(input())
for i in range(n):
    code = input()
    name = input()
    luong = int(input())
    ngayCong = int(input())
    room = map[code[3:]]
    a.append(NhanVien(code=code, name=name, room=room, luong=luong, ngayCong=ngayCong))
    
for i in a:
    print(i)