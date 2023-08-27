import functools

def cmp(a, b):
    if a["c1"] < b["c1"]: 
        return 1
    elif a["c1"] == b["c1"]:
        if a["c2"] > b["c2"]: 
            return 1
        elif a["c2"] == b["c2"]:
            if a["name"] > b["name"]: 
                return 1
            else: 
                return -1
        else: 
            return -1
    else: 
        return -1
    

student = []

t = int(input())
while t:
    name = input()
    c1, c2 = map(int, input().split())
    student.append({"name" : name,"c1" : c1, "c2" : c2})
    t -= 1

student.sort(key = functools.cmp_to_key(cmp))
for i in student:
    print(i["name"], i["c1"], i["c2"])