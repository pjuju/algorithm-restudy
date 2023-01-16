# N, K = map(int, input().split())
# values = [0]*N
# weights = [0]*N
# result = 0
#
# for i in range(N):
#     W, V = map(int, input().split())
#     weights[i] = W
#     values[i] = V
#
# def func(idx, val, wei):
#     global result
#
#     if idx == N:
#         if val > result :
#             result = val
#         return
#     if wei + weights[idx] <= K:
#         func(idx+1, val+values[idx], wei+weights[idx])
#     func(idx+1, val, wei)
#
# func(0,0,0)
# print(result)



N,K = map(int,input().split())
items = []
for _ in range(N):
    w,v = map(int,input().split())
    items.append((w,v))
dp = [0] * (K+1)
# 무게별 최대 가치
for item in items:
    w,v = item
    for i in range(K,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v)
print(dp[-1])