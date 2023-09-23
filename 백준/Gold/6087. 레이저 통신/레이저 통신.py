import sys
input = sys.stdin.readline
from collections import deque


dr, dc = [0,0,-1,1], [-1,1,0,0]

def func():
    pass


W, H = map(int, input().split())
arr = [list(input()) for _ in range(H)]
visited = [[0] * W for _ in range(H)]

sr, sc, er, ec = -1,-1,-1,-1
dq = deque()
for r in range(H):
    for c in range(W):
        if arr[r][c] == 'C':
            if sr == -1:
                sr, sc = r, c
                visited[sr][sc] = 1
                dq.append((r,c))
            else:
                er, ec = r, c

while dq:
    cr, cc = dq.popleft()
    if cr == er and cc == ec:
        print(visited[cr][cc]-2)
        break
    for x in range(4):
        nr, nc = cr+dr[x], cc+dc[x]
        while 0 <= nr < H and 0<= nc < W and arr[nr][nc] != '*':
            if not visited[nr][nc]:
                visited[nr][nc] = visited[cr][cc] + 1
                dq.append((nr, nc))
            nr, nc = nr+dr[x], nc+dc[x]