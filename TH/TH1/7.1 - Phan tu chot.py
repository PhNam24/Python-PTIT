t = int(input())
while(t):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    st = []
    l = [0] * n
    r = [0] * n
    l[0] = 1
    st.append(0)
    for i in range(1, n):
        while len(st) > 0 and a[i] >= a[st[-1]]:
            st.pop()
        if len(st) > 0:
            l[i] = i - st[-1]
        else:
            l[i] = i + 1
        st.append(i)
    r[0] = 1
    st = []
    st.append(0)
    b = list(reversed(a))
    for i in range(1, n):
        while len(st) > 0 and b[i] >= b[st[-1]]:
            st.pop()
        if len(st) > 0:
            r[i] = i - st[-1]
        else:
            r[i] = i + 1
        st.append(i)
    r.reverse()
    for i in range(n):
        if l[i] == i  + 1 and r[i] == 1:
            cnt += 1
    print(cnt)
    t -= 1