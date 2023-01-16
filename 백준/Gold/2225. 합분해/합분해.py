# def func(sum_val, cnt):
#     global result
#     if cnt == K:
#         if sum_val == N:
#             result += 1
#         return
# 
#     for num in range(N+1):
#         func(sum_val+num, cnt+1)
# 
# 


N, K = map(int, input().split())

arr = [[0] * 201 for i in range(201)]

for i in range(201):
    arr[i][1] = 1

for i in range(1, 201): # N 순회
    for j in range(201): # K 순회
        for x in range(j + 1):
            arr[j][i] += arr[x][i - 1]

print(arr[N][K] % 1000000000)



