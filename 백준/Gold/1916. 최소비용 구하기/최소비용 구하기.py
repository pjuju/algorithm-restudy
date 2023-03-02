import sys
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())
INF = 0xfffffff

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, w = map(int, input().split()) 
    graph[a].append((b,w))

start, end = map(int, input().split())
costs = [INF] * (N+1)
costs[start] = 0
hq = []
heapq.heappush(hq,(0, start))

while hq:
    cost, now = heapq.heappop(hq)
    if costs[now] < cost:
        continue

    for next, w in graph[now]:
        if costs[next] > cost+w:
            costs[next] = cost+w
            heapq.heappush(hq, (cost+w, next))

print(costs[end])

