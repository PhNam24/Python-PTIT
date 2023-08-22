n = int(input())
a = list(map(float, input().split()))
Min = 1e9
Max = -1e9
cnt = 0
for i in a:
    Min = min(Min, i)
    Max = max(Max, i)
sum = 0
for i in a:
    if i == Min: 
        continue
    elif i == Max: 
        continue
    else:
        sum += i   
        cnt += 1
print(f'{(sum / cnt):.2f}')