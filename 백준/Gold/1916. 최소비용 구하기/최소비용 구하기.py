import heapq

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))

start, end = map(int, input().split())

INF = 0xfffffff
distance = [INF] * (N+1)
distance[start] = 0
heap = []
heapq.heappush(heap, [0, start])

while heap:
    cost, to = heapq.heappop(heap)
    if distance[to] < cost:
        continue
    for new_cost, new_to in graph[to]:
        if distance[new_to] > cost+new_cost:
            distance[new_to] = cost+new_cost
            heapq.heappush(heap, [cost+new_cost, new_to])

print(distance[end])


