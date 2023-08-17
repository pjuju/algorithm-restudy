import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]

sr, sc = map(int, input().split())

visited = [[0] * N for _ in range(N)]
visited[sr-1][sc-1] = 1

dq = deque()
dq.append((sr-1,sc-1))

while dq:
    X, Y = dq.popleft()
    for nr, nc in [(X-2,Y-1), (X-2,Y+1), (X-1,Y-2), (X-1,Y+2), (X+1,Y-2), (X+1,Y+2), (X+2,Y-1), (X+2,Y+1)]:
        if 0<=nr<N and 0<=nc<N:
            if not visited[nr][nc]:
                visited[nr][nc] = visited[X][Y] + 1
                dq.append((nr,nc))

result = []
for _ in range(M):
    r,c = map(int, input().split())
    result.append(visited[r-1][c-1]-1)

print(*result)