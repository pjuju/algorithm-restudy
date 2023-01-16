N = int(input())
result = 0
for num in range(N):
    sum_v = num
    for i in str(num):
        sum_v += int(i)
    if sum_v == N:
        result = num
        break
print(result)
