
dp = [[0] * (1001) for _ in range(1001)]
dp[1][1], dp[2][1], dp[2][2], dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1, 1, 2, 1

for x in range(4, 1001):
    for y in range(1, x+1):
        dp[x][y] = (dp[x-1][y-1] + dp[x-2][y-1] + dp[x-3][y-1]) 
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())    
    print(sum(dp[n][:m+1])%1000000009)
    
