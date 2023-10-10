import sys
from collections import deque
input = sys.stdin.readline
dr, dc = [0,0,-1,1], [-1,1,0,0
                      ]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]
dq = deque()

for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            visited[i][j] = 0
        elif arr[i][j] == 2:
            dq.append((i,j))
            visited[i][j] = 0

while dq:
    cr, cc = dq.popleft()
    for x in range(4):
        nr, nc = cr+dr[x], cc+dc[x]
        if 0<=nr<N and 0<=nc<M:
            if visited[nr][nc] == -1:
                visited[nr][nc] = visited[cr][cc] + 1
                dq.append((nr,nc))

for row in visited:
    print(*row)


