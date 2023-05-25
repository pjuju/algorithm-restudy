import sys
input = sys.stdin.readline
n, k = map(int, input().split())

dp = [0] * (k+1)
dp[0] = 1

coins = [int(input()) for _ in range(n)]
for coin in coins:
    for x in range(coin,k+1):
        dp[x] += dp[x-coin]

print(dp[-1])
