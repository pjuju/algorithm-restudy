n, k = map(int, input().split())
dp = [0xfffffff] * (k+1)
dp[0] = 0

coins = [int(input()) for _ in range(n)]

for num in coins:
    for i in range(num, k+1):
        if dp[i-num] != 0xfffffff:
            dp[i] = min(dp[i], dp[i-num]+1)
            
if dp[-1] == 0xfffffff:
    print(-1)
else:
    print(dp[-1])