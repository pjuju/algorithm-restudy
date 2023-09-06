import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

N = int(input())
arr = [list(input().split()) for _ in range(N)]

blocks = []
teachers = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'X':
            blocks.append((i,j))
        elif arr[i][j] == 'T':
            teachers.append((i,j))

dr, dc = [0,0,-1,1], [-1,1,0,0] 
def check():
    
    dq = deque()
    for r,c in teachers:
        
        for x in range(4):
            dq.append((r,c,x))
        
    while dq:
        cr, cc, x = dq.popleft()    
        nr, nc = cr+dr[x], cc+dc[x]
        if 0<=nr<N and 0<=nc<N:            
            if arr[nr][nc] == 'S':
                return False
            if arr[nr][nc] != 'O':                
                dq.append((nr,nc,x))

    return True

result = 'NO'
for x in combinations(blocks, 3):
    for r,c in x:
        arr[r][c] = 'O'
    if check():
        result = 'YES'
        break
    for r,c in x:
        arr[r][c] = 'X'

print(result)
    
