from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
# 위쪽, 왼쪽
dr, dc = [-1,0,0,1], [0,-1,1,0]
# 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            si, sj = i,j
            break

queue = deque()
queue.append((si, sj, 1))
arr[si][sj] = 0
visited[si][sj] = 1
size = 2
eat = 0
result = 0
go_list = ['zzz']

while go_list:
    go_list = []
    while queue:
        r, c, cnt = queue.popleft()

        for x in range(4):
            nr, nc = r+dr[x], c+dc[x]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if arr[nr][nc] == 0 or  arr[nr][nc] == size:
                    if not go_list:
                        queue.append((nr,nc,cnt+1))
                        visited[nr][nc] = 1

                elif arr[nr][nc] < size:
                    go_list.append((nr,nc,cnt))
                    visited[nr][nc] = 1
                    break
    if go_list:
        go_list.sort(key=lambda x:(x[2],x[0],x[1]))
        nr, nc, cnt = go_list[0]
        result += cnt
        eat += 1
        if eat == size:
            size += 1
            eat = 0
        arr[nr][nc] = 0
        visited = [[0] * N for _ in range(N)]
        visited[nr][nc] = 1

        queue = deque()
        queue.append((nr, nc, 1))


print(result)







