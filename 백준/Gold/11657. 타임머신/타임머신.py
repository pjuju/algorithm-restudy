import sys
input = sys.stdin.readline
N,M = map(int, input().split())
edges = []
for _ in range(M):
    A,B,C = map(int, input().split())    
    edges.append((A,B,C))
        
INF = 0xfffffff
costs = [INF] * (N+1)
start = 1
costs[start] = 0
flag = True
for _ in range(N-1):
    for edge in edges:
        now, next, cost = edge
        if costs[now] != INF:
            if costs[next] > costs[now]+cost:
                costs[next] = costs[now]+cost

for edge in edges:
    now, next, cost = edge
    if costs[now] != INF:
        if costs[next] > costs[now]+cost:
            flag = False
            print(-1)
            break
            
if flag:
    for i in range(2, N+1):
        if costs[i] == INF:
            print(-1)
        else:
            print(costs[i])
            

    
    
