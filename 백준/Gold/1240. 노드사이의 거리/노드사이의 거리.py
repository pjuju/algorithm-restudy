from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
def func(s,e):
    dq = deque()
    dq.append((s,0))
    visited = [0] * (N+1)
    visited[s] = 1
    
    while dq:
        now, cost = dq.popleft()    
        if now == e:
            return cost 
        for n,c in graph[now]:
            if not visited[n]:
                dq.append((n,cost+c))
                visited[n] = 1
        
for _ in range(M):
    s,e = map(int, input().split())
    print(func(s,e))