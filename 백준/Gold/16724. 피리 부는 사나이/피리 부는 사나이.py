import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
parents = [i for i in range(N*M)]

dr,dc = [0,0,-1,1], [-1,1,0,0] # 좌우상하
d = {'L':0, 'R':1, 'U':2, 'D':3}

def find(a):
    if parents[a] == a:
        return a
    
    parents[a] = find(parents[a])
    return parents[a]

def union(a,b):
    pa, pb = find(a), find(b)
    if pa>pb:
        pa,pb=pb,pa
    parents[pb] = parents[pa]

for idx in range(N*M):
    r = idx // M
    c = idx % M
    
    move = d[arr[r][c]]
    nr, nc = r+dr[move], c+dc[move]
    next_idx = nr*M+nc
    if 0<=next_idx<N*M:
        union(idx, next_idx)

result = set()
for idx in range(N*M):
    result.add(find(idx))
    
print(len(result))

     
