N, M = map(int, input().split())
arr = [list(map(int,input())) for _ in range(N)]
dr = [0,0,1,-1]
dc = [1,-1,0,0]
queue = [(0,0,1)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

def bfs():
    while queue:
        r,c,d = queue.pop(0)
        if r == N-1 and c == M-1:
            return d

        for x in range(4):
            nr = r + dr[x]
            nc = c + dc[x]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                if not visited[nr][nc]:
                    queue.append((nr,nc,d+1))
                    visited[nr][nc] = 1
    
result = bfs()

print(result)
