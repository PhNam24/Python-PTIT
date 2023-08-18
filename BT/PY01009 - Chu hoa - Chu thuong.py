s = input()
d = 0
for i in s:
    if i >= 'a' and i <= 'z': d += 1
    else: d -= 1
if d >= 0: print(s.lower())
else: print(s.upper()) 