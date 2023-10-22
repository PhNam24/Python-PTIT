n = int(input())

ans = 0
st = []
d = {}
for i in range(n):
    a = int(input())
    while st and a > st[-1]:
        d[st[-1]] -= 1
        st.pop()
        ans += 1
    if len(st):
        if a == st[-1]:
            ans += d[a] + (len(st) > d[a])
        else:
            ans += 1
    st.append(a)
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
print(ans)