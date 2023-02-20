import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [1]*(N+1)

for i in range(1, N+1):
    dp[i] = dp[i-1]
    if i-M >= 0:
        dp[i] += dp[i-M]
    dp[i] %= 1000000007

print(dp[N])