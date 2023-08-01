import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
poss = list(map(int, input().split()))
poss[N-1] = 0
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int, input().split())
    if not poss[a] and not poss[b]: 
        graph[a].append((b,c))
        graph[b].append((a,c))

INF = 1e18
distance = [INF] * N
distance[0] = 0
hq = []
hq.append((0,0))

while hq:
    now, nc = heapq.heappop(hq)
 
    if distance[now] < nc:
        continue
 
    for next,cost in graph[now]:        
        if distance[next] > nc + cost:
            distance[next] = nc + cost
            heapq.heappush(hq, (next,nc + cost))

print(-1 if distance[N-1] == 1e18 else distance[N-1])
