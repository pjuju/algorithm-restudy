import sys
read = sys.stdin.readline
from collections import deque

def bfs():
    while queue:
        a = queue.popleft()
        r = a[0]
        c = a[1]
        for i in range(4):
           nr = r + dr[i]
           nc = c + dc[i]
           if 0 <= nr < M and 0 <= nc < N:
               if arr[nr][nc] == 0:
                   arr[nr][nc] = arr[r][c] + 1
                   queue.append([nr, nc])


N,M = map(int, read().split())
arr = [list(map(int, read().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
queue = deque([])
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            queue.append([i,j])
dr = [0,0,-1,1]
dc = [1,-1,0,0]

bfs()
result = 0

for i in range(M):
    for j in range(N):
        if arr[i][j]-1 > result:
            result = arr[i][j] - 1

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            result = -1
            break

print(result)






