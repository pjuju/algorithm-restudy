import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

s, e = map(int, input().split())

pre = [i for i in range(n+1)]

distance = [float('inf')] * (n+1)
distance[s] = 0

hq = []
visit = set()
heapq.heappush(hq, (0,s))

while hq:
    cost, now = heapq.heappop(hq)
    if distance[now] != cost:
        continue
    
    if now == e:
        route = [e]
        while now != s:
            route.append(pre[now])
            now = pre[now]

        print(cost)
        print(len(route))
        print(*route[::-1])
        
        break

    for next, nc in graph[now]:
        if distance[next] > cost+nc:
            distance[next] = cost+nc
            pre[next] = now
            heapq.heappush(hq, (nc+cost, next))
