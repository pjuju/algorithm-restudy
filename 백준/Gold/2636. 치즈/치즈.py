import sys
from collections import deque
input = sys.stdin.readline
dr, dc = [1,-1,0,0], [0,0,1,-1]
R, C = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

outside = deque()
outside.append((0,0))
visited[0][0] = 1

time = 0
result = 0
while outside:
    result = len(outside)
    time += 1 
    dq = deque()   
    while outside:
        dq.append(outside.popleft())
    while dq:
        r,c = dq.popleft()    
        for x in range(4):
            nr, nc = r+dr[x], c+dc[x]
            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc]:                    
                    if arr[nr][nc]:
                        outside.append((nr,nc))
                        arr[nr][nc] = time
                    else:
                        dq.append((nr,nc))
                    visited[nr][nc] = 1
print(time-1)
print(result)