str  = input()
arr = []
for i in str:
    if i.isalnum(): arr.append(int(i))

if arr[0] + arr[1] == arr[2]: print("YES")
else: print("NO")
