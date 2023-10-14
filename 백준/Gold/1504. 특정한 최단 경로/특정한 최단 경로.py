import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

x, y = map(int, input().split())

def func(a):
    distance = [float('inf')] * (N+1)
    distance[a] = 0
    hq = []
    heapq.heappush(hq, (0,a))

    while hq:
        cost, now = heapq.heappop(hq)
        if distance[now] != cost:
            continue
        for next,nc in graph[now]:
            if distance[next] > cost+nc:
                distance[next] = cost+nc
                heapq.heappush(hq, (cost+nc, next))

    return distance


distance_x = func(x)
distance_y = func(y)

result = distance_x[y] + min(distance_x[1]+distance_y[N], distance_x[N]+ distance_y[1])
if result >= float('inf'):
    print(-1)
else:
    print(result)