class Tram:
    def __init__(self, stt, name, luongMua, thoiGian):
        self.code = "T"
        if stt < 10:
            self.code += "0" + str(stt)
        else:
            self.code += str(stt)
        self.name = name
        self.luongMua = luongMua
        self.tongTime = thoiGian
        self.muaTB = 0
   
    def getName(self):
        return self.name
   
    def update(self, luongMua, thoiGian):
        self.luongMua += luongMua
        self.tongTime += thoiGian
    
    def updateTB(self):
        self.muaTB = self.luongMua / self.tongTime
    
    def __str__(self) -> str:
        return self.code + " " + self.name + f"{self.muaTB: .2f}"
    
t = int(input())
a = []
nameList = []
for i in range(t):
    name = input()
    start = list(map(int, input().split(":")))
    end = list(map(int, input().split(":")))
    luongMua = int(input())
    time = 0
    if end[1] < start[1]:
        time = (end[0] - start[0] - 1) + (end[1] - start[1] + 60) / 60
    else:
        time = end[0] - start[0] + (end[1] - start[1]) / 60
    if name not in nameList:
        a.append(Tram(i + 1, name=name, luongMua=luongMua, thoiGian=time))
        nameList.append(name)
    else:
        for j in a:
            if j.getName() == name:
                j.update(luongMua, time)
    
for i in a:
    i.updateTB()
    print(i)
    