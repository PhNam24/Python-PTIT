s = input()
st = []
st.append(-1)
ans = []
for i in range(len(s)):
    if s[i] == '(':
        st.append(i)
    else:
        st.pop()
        if len(st) > 0:
            tmp = ""
            for j in range(st[-1] + 1, i + 1):
                tmp += s[j]
            ans.append(tmp)
        else:
            st.append(i)
ans.sort()
print(ans[len(ans) - 1])

#de ma ma chung may