from itertools import combinations
import copy

dr, dc = [-1,1,0,0], [0,0,-1,1]
def func(r,c):
    global cnt
    if cnt >= virus_cnt:
        return
    for k in range(4):
        nr, nc = r+dr[k], c+dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if new_arr[nr][nc] == 0 and not visited[nr][nc]:
                new_arr[nr][nc] = 2
                visited[nr][nc] = 1
                cnt += 1
                func(nr,nc)




N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus_cnt = 0xffffffff
zeros,virus = [], []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zeros.append((i,j))
        if arr[i][j] == 2:
            virus.append((i,j))

zeros_three = list(combinations(zeros,3))
for z in zeros_three:
    new_arr = copy.deepcopy(arr)

    for r,c in z:
        new_arr[r][c] = 1

    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for r,c in virus:
        func(r,c)

    if cnt < virus_cnt:
        virus_cnt = cnt

print(len(zeros)-virus_cnt-3)



