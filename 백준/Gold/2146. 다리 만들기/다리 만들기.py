import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dr, dc = [0,0,-1,1], [-1,1,0,0]

def func(r,c,x):
    tmp = []
    num_arr[r][c] = x
    dq = deque()
    dq.append((r,c))
    
    
    while dq:
        cr, cc = dq.popleft()
        tmp.append((cr,cc))
        for d in range(4):
            nr, nc = cr+dr[d], cc+dc[d]
            if 0<= nr< N and 0<=nc<N:
                if arr[nr][nc] and not num_arr[nr][nc]:
                    num_arr[nr][nc] = x
                    dq.append((nr,nc))

    ent_lst.append(tmp)           

num_arr = [[0] * N for _ in range(N)]
ent_lst = []
x = 1
for r in range(N):
    for c in range(N):
        if arr[r][c] and not num_arr[r][c]:
            func(r,c,x)
            x += 1

result = float('inf')
for i in range(len(ent_lst)):
    for j in range(i+1, len(ent_lst)):
        for ar, ac in ent_lst[i]:
            for br, bc in ent_lst[j]:
                result = min(result, abs(ar-br)+abs(ac-bc)-1)

print(result)
