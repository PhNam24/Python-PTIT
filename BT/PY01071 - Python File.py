s = input().lower()
s = s[len(s) - 3:]
if s != '.py':
    print("no")
else:
    print("yes")