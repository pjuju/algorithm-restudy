import sys
input = sys.stdin.readline
n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [k+1] * (k+1)
dp[0] = 0
for coin in coins:
    for x in range(coin, k+1):
        dp[x] = min(dp[x], dp[x-coin]+1)


print(-1 if dp[-1] == k+1 else dp[-1])

