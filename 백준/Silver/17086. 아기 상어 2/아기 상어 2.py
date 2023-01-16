from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

shark = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            shark.append((i,j))

# 상 하 좌 우 상좌 상우 하좌 하우
dr, dc = [1,-1,0,0,1,1,-1,-1], [0,0,-1,1,-1,1,-1,1]
result = 1
while shark:
    r,c = shark.popleft()
    if arr[r][c] > result:
        result = arr[r][c]
    for x in range(8):
        nr, nc = r+dr[x], c+dc[x]
        if 0<= nr < N and 0<= nc < M:
            if not arr[nr][nc]:
                arr[nr][nc] = arr[r][c] + 1
                shark.append((nr,nc))
print(result-1)
