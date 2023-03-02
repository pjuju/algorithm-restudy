import sys
input = sys.stdin.readline
import heapq

n,m,k = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = 0xffffffffff
costs = [[INF] * (k) for _ in range(n+1)]
start = 1
costs[1][0] = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

hq = []
heapq.heappush(hq, (0, start))

while hq:
    now_cost, now = heapq.heappop(hq)   

    for next, cost in graph[now]:
        if costs[next][k-1] > now_cost+cost:
            costs[next][k-1] = now_cost+cost
            costs[next].sort() 
            heapq.heappush(hq, (now_cost+cost, next))


for i in range(1, n+1):
    if costs[i][k-1] == INF:
        print(-1)
    else:
        print(costs[i][k-1])
