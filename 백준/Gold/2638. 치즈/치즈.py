import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = [[2] * M for _ in range(N)]

dr, dc = [0,0,-1,1], [-1,1,0,0]

airs = set()
def air_add(r,c):
    
    airs.add((r,c))
    dq = deque()
    dq.append((r,c))

    while dq:
        cr, cc = dq.popleft()
        for x in range(4):
            nr, nc = cr+dr[x], cc+dc[x]
            if 0<=nr<N and 0<=nc<M:
                if not arr[nr][nc]:
                    if (nr,nc) not in airs:
                        airs.add((nr,nc))
                        dq.append((nr,nc))
              
                    
air_add(0,0)
visit = set()
time = 0
while len(airs) != N*M:
    time += 1
    tmp = list(airs)
    for r,c in tmp:
        if (r,c) not in visit:
            visit.add((r,c))
            for x in range(4):
                nr, nc = r+dr[x], c+dc[x]
                if 0<=nr<N and 0<=nc<M:
                    if arr[nr][nc]:
                        cnt[nr][nc] -= 1
                        if cnt[nr][nc] == 0:
                            air_add(nr,nc)
print(time)
    



        