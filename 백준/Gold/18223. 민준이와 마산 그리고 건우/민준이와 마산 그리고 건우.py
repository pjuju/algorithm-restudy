import sys
import heapq
input = sys.stdin.readline

V,E,P = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance = [sys.maxsize] * (V+1)
distance[1] = 0
hq = []
heapq.heappush(hq, (0,1))

while hq:
    cost, now = heapq.heappop(hq)
    for next,nc in graph[now]:        
        if distance[next] >= cost + nc:                
            distance[next] = cost + nc
            heapq.heappush(hq, (distance[next], next))

p_distance = [sys.maxsize] * (V+1)
p_distance[P] = 0
hq = []
heapq.heappush(hq, (0,P))

while hq:
    cost, now = heapq.heappop(hq)
    for next,nc in graph[now]:        
        if p_distance[next] >= cost + nc:                
            p_distance[next] = cost + nc
            heapq.heappush(hq, (p_distance[next], next))

if distance[P] + p_distance[V] == distance[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")
    


