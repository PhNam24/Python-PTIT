def check(s):
    sum = int(s[len(s) - 1]);
    for i in range(len(s) - 1):
        if abs(int(s[i]) - int(s[i + 1])) != 2:
            return "NO"
        sum += int(s[i])
    if sum % 10 != 0:
        return "NO"
    return "YES"

t = int(input())
while t:
    n = input()
    print(check(n))
    t -= 1