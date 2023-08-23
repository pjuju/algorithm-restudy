import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for r in  range(N):
    for c in range(N):
        if dp[r][c] and arr[r][c]:
            nr, nc = r+arr[r][c], c+arr[r][c]
            if nr < N:
                dp[nr][c] += dp[r][c]
            if nc < N:
                dp[r][nc] += dp[r][c]

print('HaruHaru' if dp[N-1][N-1] else 'Hing')
