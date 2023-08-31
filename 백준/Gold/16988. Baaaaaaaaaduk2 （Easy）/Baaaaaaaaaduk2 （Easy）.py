import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr, dc = [0,0,-1,1], [1,-1,0,0]

zeros = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zeros.append((i,j))
            
def bfs(r,c, visited):
    dq = deque()
    dq.append((r,c))
    visited[r][c] = 1
    cnt = 0
    flag = True
    while dq:
        cr, cc = dq.popleft()
        cnt += 1
        for x in range(4):
            nr, nc = cr+dr[x], cc+dc[x]
            if 0<=nr<N and 0<=nc<M:
                if arr[nr][nc] == 0:
                    flag = False
                elif arr[nr][nc] == 2 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    dq.append((nr, nc))
    if flag:
        return cnt    
    else:
        return 0
    
def func(lst):
    
    visited = [[0] * M for _ in range(N)]
    for r, c in lst:
        arr[r][c] = 1

    val = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2 and not visited[i][j]:
                val += bfs(i,j, visited)
        
    for r,c in lst:
        arr[r][c] = 0

    return val

result = 0
for lst in combinations(zeros, 2):
    result = max(func(lst), result)

print(result)
    
    