import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0] * (K+1)

for _ in range(N):
    w,v = map(int, input().split())

    for x in range(K, w-1, -1):
        if dp[x-w] + v > dp[x]:
            dp[x] = dp[x-w] + v 
            
print(dp[-1])
