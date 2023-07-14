N = int(input())
result = 0
dp = [[0] * 10 for _ in range(N)]
for x in range(1,10):
    dp[0][x] = 1

for n in range(1,N):
    for x in range(10):
        for px in (x-1,x+1):
            if 0<=px<10:
                dp[n][x] += dp[n-1][px]

print(sum(dp[N-1])%1000000000)
