file = open("D:\Code\CodePTIT\Python-PTIT\BT\InputFile\CONTACT.in", "r")

set = set()

for i in file:
    set.add(i.lower().strip())

ans = sorted(set)

for i in ans:
    print(i)
    
