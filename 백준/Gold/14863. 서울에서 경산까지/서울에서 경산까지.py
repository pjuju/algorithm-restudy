import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    a, a_val, b, b_val = map(int, input().split())
    
    for x in range(K-a+1):
        if dp[i-1][x]:
            dp[i][x+a] = max(dp[i][x+a],dp[i-1][x] + a_val)

    for x in range(K-b+1):
        if dp[i-1][x]:
            dp[i][x+b] = max(dp[i][x+b],dp[i-1][x] + b_val)

print(max(dp[N])-1)