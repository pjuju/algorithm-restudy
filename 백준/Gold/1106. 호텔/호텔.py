import math

C, N = map(int, input().split())
dp = [1e7] * (C+101)
dp[0] = 0
for _ in range(N):
    cost, people = map(int, input().split())
    if dp[people] > cost:
        dp[people] = cost

for p in range(C+101):
    for x in range(p//2+1):
        if dp[p] > dp[x] + dp[p-x]:
            dp[p] = dp[x] + dp[p-x]

print(min(dp[C:]))


