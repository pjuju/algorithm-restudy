from collections import deque
import sys
input = sys.stdin.readline

N,M,A,B = map(int, input().split())
dr, dc = [1,0], [0,1] # 오른쪽, 아래쪽
hole = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]
items = [(N-1,M-1)]

for _ in range(A):
    r,c = map(int, input().split())    
    items.append((r-1,c-1))
items.sort()

for _ in range(B):
    r,c = map(int, input().split())
    hole[r-1][c-1] = 1

dp[0][0] = 1
dq = deque()
dq.append((0,0))
for (tr,tc) in items:
    while dq:
        r,c = dq.popleft()
        if r == tr and c == tc:
            dq.clear()
            dq.append((r,c))
            break
        
        for x in range(2):
            nr, nc = r+dr[x], c+dc[x]
            if nr <= tr and nc <= tc:
                if not hole[nr][nc]:
                    if not dp[nr][nc]:
                        dq.append((nr,nc))
                    dp[nr][nc] += dp[r][c]
                    
print(dp[N-1][M-1])

                        
                    
    

    