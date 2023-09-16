file = open("D:\Code\CodePTIT\Python-PTIT\TH\TH1\CONTACT.in", "r")

s = set()

for i in file:
    s.add(i.lower().strip())

s = sorted(s)
for i in s:
    print(i)