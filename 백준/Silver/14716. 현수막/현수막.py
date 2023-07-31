M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dr, dc = [0,0,-1,1,1,1,-1,-1], [1,-1,0,0,1,-1,1,-1] 
def func(r,c):
    queue = [(r,c)]
    visited[r][c] = 1
    while queue:
        rr, cc = queue.pop()
        for x in range(8):
            nr, nc = rr + dr[x], cc + dc[x]
            if 0 <= nr < M and 0 <= nc < N:
                if not visited[nr][nc] and arr[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr,nc))


result = 0
visited = [[0] * N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if not visited[i][j] and arr[i][j]:
            result += 1
            func(i,j)

print(result)