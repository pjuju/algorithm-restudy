import sys
input = sys.stdin.readline
from collections import deque

N, start, end, M = map(int, input().split())
INF = 0xffffffff
edges = []

for _ in range(M):
    a,b,c = map(int, input().split())
    edges.append([a,b,c])
  
earns = list(map(int, input().split()))

for i in range(M):
    now, next, cost = edges[i]
    edges[i][2] = -cost + earns[next]

results = [-INF] * (N)
results[start] = earns[start]

for i in range(N-1):
    for edge in edges:
        now, next, cost = edge[0], edge[1], edge[2]
        if results[now] != -INF:
            if results[next] < results[now] + cost:
                results[next] = results[now] + cost

def check(start, end):
    queue = deque([start])
    visited = [0] * (N)
    visited[start] = 1
    while queue:
        now = queue.popleft()
        if now == end:
            return False
        
        for edge in edges:
            if edge[0] == now:
                if not visited[edge[1]]:
                    queue.append(edge[1])
                    visited[edge[1]] = True
    
    return True

flag = True
for edge in edges:
    now, next, cost = edge[0], edge[1], edge[2]
    if results[now] != -INF:
        if results[next] < results[now] + cost:
            results[next] = results[now] + cost
            flag = check(next, end)
            if not flag:
                print("Gee")
                break
            
if flag:
    if results[end] != -INF:
        print(results[end])
    else:
        print('gg')
