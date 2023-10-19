import sys
input = sys.stdin.readline
from collections import deque
import heapq

N, M = map(int, input().rstrip().split())
dr, dc = [0,0,-1,1], [-1,1,0,0]
arr = [list(map(int, input().split())) for _ in range(N)]
visit = set()
islands = []

def add_island(r,c):
    dq = deque()
    dq.append((r,c))
    visit.add((r,c))
    island = []
    while dq:
        cr, cc = dq.popleft()
        island.append((cr,cc))
        for x in range(4):
            nr, nc = cr+dr[x], cc+dc[x]
            if 0<=nr<N and 0<=nc<M:
                if arr[nr][nc] and (nr,nc) not in visit:
                    visit.add((nr,nc))
                    dq.append((nr,nc))
    islands.append(island)

def cal_d(i,j):
    dq = deque()
    for r,c in islands[i]:
        for x in range(4):
            dq.append((r,c,0,x))
    while dq:
        cr, cc, c, x = dq.popleft()
       
        nr, nc = cr+dr[x], cc+dc[x]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 0:
                dq.append((nr,nc,c+1,x))
            else:
                if (nr,nc) in islands[j]:
                    if c > 1:
                        distance[i][j] = c
                        distance[j][i] = c
                        return
   

for r in range(N):
    for c in range(M):
        if arr[r][c] and (r,c) not in visit:
            add_island(r,c)
    
i_l = len(islands)
distance = [[float('inf')] * i_l for _ in range(i_l)]

for i in range(i_l):
    for j in range(i+1, i_l):
        cal_d(i,j)


costs = [float('inf')] * i_l
costs[0] = 0
hq = []
heapq.heappush(hq, (0,0))
visits = set()
visits.add(0)
while hq:
    cost, now = heapq.heappop(hq)
    if costs[now] < cost:
        continue
    visits.add(now)

    for n in range(1, i_l):
        if n not in visits and costs[n] > distance[now][n]:
            costs[n] = distance[now][n]
            heapq.heappush(hq, (distance[now][n], n))


result = sum(costs)
print(result if result < float('inf') else -1)
