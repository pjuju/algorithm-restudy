import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

sr, sc, er, ec = 0,0,0,0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S':
            sr, sc = i,j
        elif arr[i][j] == 'F':
            er, ec = i,j
            
inf = 10000
dq = deque() 
dp = [[(inf,inf)] * M for _ in range(N)]
dp[sr][sc] = (0,0)

dq.append((sr,sc,0,0))

dr, dc = [0,0,-1,1], [-1,1,0,0]
while dq:
    cr, cc, x, y = dq.popleft()

    if dp[cr][cc] != (x,y):
        continue

    for d in range(4):
        nr, nc, nx, ny = cr+dr[d], cc+dc[d], x, y
        if 0<=nr<N and 0<=nc<M:
            if arr[nr][nc] == 'g':
                nx += 1
            elif arr[nr][nc] == '.':
                for dd in range(4):
                    nnr, nnc = nr+dr[dd], nc+dc[dd]
                    if 0<=nnr<N and 0<=nnc<M:
                        if arr[nnr][nnc] == 'g':
                            ny += 1
                            break
                        
            px, py = dp[nr][nc]
            
            if nx < px:
                dp[nr][nc] = (nx, ny)
                dq.append((nr,nc,nx,ny))
                
            elif nx == px and ny < py:
                dp[nr][nc] = (nx, ny)
                dq.append((nr,nc,nx,ny))
                
a,b = dp[er][ec]
# for x in range(4):
#     r, c = er + dr[x], ec + dc[x]
#     if 0 <= r < N and 0<=c<M:
#         if arr[r][c] == 'g':
#             b -= 1
#             break    
print(a,b)