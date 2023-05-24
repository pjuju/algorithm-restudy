import heapq
import sys
input = sys.stdin.readline
N,M,A,B,C = map(int, input().split())
INF = sys.maxsize

def dijk(val):
    distance = [INF] * (N+1)
    distance[A] = 0
    hq = [(0,A)]
    while hq:
        cost, now = heapq.heappop(hq)
        if cost > C:
            return False
        if now == B:
            return True
        if cost > distance[now]:
            continue
        for next, nc in graph[now]:
            if nc <= val:
                if distance[next] > cost+nc:      
                    distance[next] = cost+nc        
                    heapq.heappush(hq,(cost+nc, next))

    return False

max_cost = 0
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    if c > max_cost:
        max_cost = c
        
left, right = 0, max_cost

ans = -1
while left <= right:
    mid = (left+right)//2
    if dijk(mid):
        ans = mid
        right = mid-1
    else:
        left = mid+1
        
print(ans)