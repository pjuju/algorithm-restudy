import sys
input = sys.stdin.readline
from collections import deque

M, N= map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr, dc = [0,-1,0,1], [-1,0,1,0]

blocks = [[(0,0)] * M for _ in range(N)]
counts = [[0] * M for _ in range(N)]

def func(r,c):
    dq = deque()
    visit.add((r,c))
    dq.append((r,c))
    count = 1
    while dq:
        cr, cc = dq.popleft()
        blocks[cr][cc] = (r,c)
        v = arr[cr][cc]
        for x in range(3,-1,-1):            
            if v >= 2**x:
                v -= 2**x
            else:
                nr, nc = cr+dr[x], cc+dc[x]     
                if (nr,nc) not in visit:
                    visit.add((nr,nc))
                    dq.append((nr,nc))                 
                    count += 1
    counts[r][c] = count

visit = set()
for r in range(N):
    for c in range(M):
        if (r,c) not in visit:
            func(r,c)
        
result = set()
max_v = 0
max_vv = 0
for r in range(N):
    for c in range(M):
        a,b = blocks[r][c]
        cnt = counts[a][b]
        v = arr[r][c]
        for x in range(3,-1,-1):            
            if v >= 2**x:
                v -= 2**x
                nr, nc = r+dr[x], c+dc[x]
                if 0<=nr<N and 0<=nc<M:
                    aa,bb = blocks[nr][nc]
                    if aa != a or bb != b:
                        max_vv = max(max_vv, cnt+counts[aa][bb])
        if (a,b) not in result:
            result.add((a,b))
            max_v = max(max_v, cnt)
            
print(len(result))
print(max_v)
print(max_vv)


