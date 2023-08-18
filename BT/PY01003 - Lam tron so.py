t = int(input())
while t:
    n = int(input())
    if n <= 10: 
        print(n, end="")
    else:
        arr = []
        while(n):
            tmp = n % 10
            arr.append(tmp)
            n //= 10
        arr.reverse()
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] >= 5: arr[i - 1] += 1
            arr[i] = 0
        for i in arr: print(i, end = "", sep = "")
    print("\n")
    t -= 1