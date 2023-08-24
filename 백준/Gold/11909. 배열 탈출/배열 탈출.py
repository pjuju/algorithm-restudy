import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[1e9] * N for _ in range(N)]
dp[0][0] = 0

for x in range(1, N):
    # c_cost = max(0,arr[0][x] + 1 - arr[0][x-1])
    dp[0][x] = dp[0][x-1] + max(0,arr[0][x] + 1 - arr[0][x-1])

    # r_cost = max(0, arr[x][0] + 1 - arr[x-1][0])
    dp[x][0] = dp[x-1][0] + max(0, arr[x][0] + 1 - arr[x-1][0])


for r in range(1,N):
    for c in range(1,N):
        r_cost,c_cost = max(0,arr[r][c]-arr[r-1][c]+1), max(0,arr[r][c]-arr[r][c-1]+1)
        dp[r][c] = min(dp[r][c], dp[r-1][c]+r_cost, dp[r][c-1]+c_cost)

print(dp[-1][-1])