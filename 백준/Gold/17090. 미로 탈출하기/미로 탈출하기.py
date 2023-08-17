import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dq = deque()
for r in range(N):
    dq.append((r,-1))
    dq.append((r,M))
for c in range(M):
    dq.append((-1,c))
    dq.append((N,c))

dr, dc = [-1,1,0,0],[0,0,-1,1]
reverse_dir = {'U':1, 'D':0, 'L':3, 'R':2}
cnt = 0
while dq:
    cr, cc = dq.popleft()
    for x in range(4):
        nr, nc = cr+dr[x], cc+dc[x]
        if 0<=nr<N and 0<=nc<M:
            dir = arr[nr][nc]
            if x == reverse_dir[dir]:
                dq.append((nr,nc))
                cnt += 1
                
print(cnt)
    
