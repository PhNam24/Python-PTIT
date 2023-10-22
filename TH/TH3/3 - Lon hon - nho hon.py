def bfs(x):
    check = [0] * 100005
    count = 0
    q = []
    q.append(1)
    while len(q):
        tmp = q.pop(0)
        check[tmp] = 1
        count += 1
        for i in ke[tmp]:
            if check[i] == 0:
                q.append(i)
                check[i] = 1
            else: 
                if i == x:
                    return True
    return False

def kahn():
    q = []
    for i in range(1, cnt):
        if degree[i] == 0:
            q.append(i)
    count = 0
    while len(q):
        tmp = q.pop(0)
        count += 1
        for i in ke[tmp]:
            degree[i] -= 1
            if degree[i] == 0:
                q.append(i)
    if count == cnt - 1:
        return False
    return True

n = int(input())
d = {}
cnt = 1 
ke = [[] for i in range(100005)]
degree = [0] * 100005
for i in range(n):
    name1, dau, name2 = input().split()
    if name1 not in d:
        d[name1] = cnt 
        cnt += 1
    if name2 not in d:
        d[name2] = cnt
        cnt += 1
    if dau == '>':
        ke[d[name1]].append(d[name2])
        degree[d[name2]] += 1
    else:
        ke[d[name2]].append(d[name1])
        degree[d[name1]] += 1

if kahn():
    print("impossible")
else:
    print("possible")