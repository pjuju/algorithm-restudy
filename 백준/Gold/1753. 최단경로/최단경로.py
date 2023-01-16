import heapq
V, E = map(int, input().split())
start = int(input())
graphs = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graphs[u].append((v,w))


INF = 0xfffff
dp = [INF] * (V+1)
dp[start] = 0

heap = []
heapq.heappush(heap, (0,start))

while heap:
    cost, node = heapq.heappop(heap)

    for v,w in graphs[node]:
        if w + cost < dp[v]:
            dp[v] = w+cost
            heapq.heappush(heap, (cost+w, v))

for i in range(1, V+1):
    print(dp[i] if dp[i] != INF else "INF")
