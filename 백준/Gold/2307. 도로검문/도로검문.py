import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

parents = [0] * (N+1)

def djik(a,b):
    hq = []
    heapq.heappush(hq, (0,1))
    dist = [1e9] * (N+1)
    dist[1] = 0

    while hq:
        d, now = heapq.heappop(hq)

        if dist[now] < d :
            continue

        for next, nc in graph[now]:
            if (a == now and b == next) or (a == next and b == now):
                continue
            if dist[next] > d + nc:
                heapq.heappush(hq, (d+nc, next))
                dist[next] = d + nc
                if not a:
                    parents[next] = now
    return dist[N]

val = djik(0,0)
result = -1

s = N
while parents[s]:
    
    e = parents[s]
    v = djik(s,e)
    if v != 1e9:
        if v - val > result:
            result = v-val
    else:
        result = -1
        break
    s = e

print(result)