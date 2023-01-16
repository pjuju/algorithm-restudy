from itertools import combinations
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chickens = []
homes = []
result = 0xffffff
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chickens.append((i,j))
        if arr[i][j] == 1:
            homes.append((i, j))

dr, dc = [1,-1,0,0], [0,0,-1,1]
def func(lst):

    distance = 0
    visited = [[0]*N for _ in range(N)]
    for r,c in lst:
        visited[r][c] = 1
    while lst:
        r,c = lst.pop(0)
        for x in range(4):
            nr,nc = r+dr[x], c+dc[x]
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                lst.append((nr,nc))
    for r,c in homes:
        distance += (visited[r][c] - 1)


    global result
    if distance < result:
        result = distance


for lst in combinations(chickens,M):
    func(list(lst))

print(result)
