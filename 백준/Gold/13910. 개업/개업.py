import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(M):
    for j in range(i+1, M):
        if lst[i]+lst[j] <= N:
            lst.append(lst[i]+lst[j])

dp = [1e18] * (N+1)
lst = list(set(lst))

for a in lst:
    dp[a] = 1

for x in range(1, N+1):
    for y in lst:        
        if x-y > 0:
            if dp[x] > dp[x-y] + dp[y]:
                dp[x] = dp[x-y] + dp[y]

print(dp[-1] if dp[-1] != 1e18 else -1)