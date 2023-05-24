import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())

no_road = set()
for _ in range(K):
    ar,ac,br,bc = map(int, input().split())
    if ar+ac > br+bc:
        ar,ac,br,bc = br,bc,ar,ac
    no_road.add((ar,ac,br,bc))
    
dp = [[0] * (M+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    if (i-1,0,i,0) in no_road:
        break
    dp[i][0] = 1
for i in range(1, M+1):
    if (0,i-1,0,i) in no_road:
        break
    dp[0][i] = 1

dr, dc = [0,-1],[-1,0]
for r in range(1,N+1):
    for c in range(1,M+1):
        for x in range(2):
            nr, nc = r+dr[x], c+dc[x]
            if (nr,nc,r,c) not in no_road:
                dp[r][c] += dp[nr][nc]
        
print(dp[-1][-1])
