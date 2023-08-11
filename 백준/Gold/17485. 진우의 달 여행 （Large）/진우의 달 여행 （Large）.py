import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[100001] * M for _ in range(N)] for _ in range(3)]

for x in range(3):
    for c in range(M):
        dp[x][0][c] = arr[0][c]

for r in range(1, N):
    for c in range(M):
        for x in range(3): # 방향        
            pc = c-x+1 # 이전 c
            if 0<=pc<M:            
                for y in range(3):
                    if x != y:                                                        
                        dp[x][r][c] = min(dp[x][r][c], dp[y][r-1][pc] + arr[r][c])
answer = 100001        
for x in range(3):
    for c in range(M):
        answer = min(answer, dp[x][N-1][c])            

print(answer)