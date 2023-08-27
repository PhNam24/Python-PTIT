import re

s = ""
while 1:
    try:
        s += input()
    except EOFError:
        break

s = re.split(r'[\.\?\!]', s)

for i in range(len(s) - 1):
    tmp = s[i].lower().split()
    tmp[0] = tmp[0].title()
    print(*tmp)