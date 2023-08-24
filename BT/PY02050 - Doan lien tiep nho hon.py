t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    st = []
    st.append(0)
    ans = [0] * n
    for i in range(n):
        while(len(st) and a[i] >= a[st[-1]]):
            st.pop()
        if(len(st)):
            ans[i] = i - st[-1]
        else:
            ans[i] = i + 1
        st.append(i)
    for i in range(n):
        print(ans[i], end = " ")
    print()
    t -= 1