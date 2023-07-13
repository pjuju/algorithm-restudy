from itertools import combinations
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus = []
count = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append((i,j))
            count += 1
        if arr[i][j] == 0:            
            count += 1

result = N**2
dr, dc = [-1,1,0,0], [0,0,-1,1]

def func(comb):
    global result

    dq = deque()
    visited = [[0] * N for _ in range(N)]
    for i,j in comb:
        dq.append((i,j))
        visited[i][j] = 1
    
    t = 0
    cnt = 0
    while dq:
        r,c = dq.popleft()
        cnt += 1
        t = visited[r][c] - 1
        if t >= result:
            return
        for x in range(4):
            nr, nc = r+dr[x], c+dc[x]
            if 0<=nr<N and 0<=nc<N:
                if arr[nr][nc] != 1 and not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    dq.append((nr,nc))
                   
    if cnt == count:
        result = t


for C in combinations(virus, M):
    func(C)

if result == N**2:
    print(-1)
else:
    print(result)