from collections import deque
N, M = map(int, input().split())

lst = [0] * (N+1)
for _ in range(M):
    a = int(input())
    lst[a] = 1

dp = [[10001] * (int((2*N)**0.5)+2) for _ in range(N+1)]
dp[1][0] = 0
for i in range(2, N+1):
    if not lst[i]:
        for x in range(1, int((2*i)**0.5)+1):       
                dp[i][x] = min(dp[i-x][x-1], dp[i-x][x], dp[i-x][x+1]) + 1

ans = min(dp[N])
if ans >= 10001:
    print(-1)
else:        
    print(ans)