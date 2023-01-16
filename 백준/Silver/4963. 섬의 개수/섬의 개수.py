dr, dc = [0,0,-1,1,1,1,-1,-1], [1,-1,0,0,1,-1,1,-1]

def dfs(r,c):
    visited[r][c] = 1
    for x in range(8):
        nr, nc = r + dr[x], c + dc[x]
        if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == 1 and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc)





while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    lands = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                lands.append((i,j))

    visited = [[0] * w for _ in range(h)]

    result = 0
    for i,j in lands:
        if not visited[i][j]:
            result += 1
            dfs(i,j)

    print(result)

