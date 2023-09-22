import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [list(input()) for _ in range(N)]
new_arr = [[0] * N for _ in range(N)]
result = [0,0]

dr, dc = [0,0,-1,1], [-1,1,0,0]
def func(r,c,array):
    visited[r][c] = 1
    for x in range(4):
        nr, nc = r+dr[x], c+dc[x]
        if 0<=nr<N and 0<=nc<N:
            if array[nr][nc] == array[r][c]:
                if not visited[nr][nc]:
                    func(nr,nc,array)


visited = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if arr[r][c] == 'B':
            new_arr[r][c] = 1
        if not visited[r][c]:
            result[0] += 1
            func(r,c,arr)

visited = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            result[1] += 1
            func(r,c,new_arr)

print(*result)