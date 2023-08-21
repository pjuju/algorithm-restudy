import sys
input = sys.stdin.readline
import heapq 

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for i in range(N+1):
    graph[i].sort()

s, e = map(int, input().split())

def djik(visited, x):
    distance = [1e9]*(N+1)
    distance[x] = 0
    hq = []
    heapq.heappush(hq, (0,x))
    while hq:
        cost, now = heapq.heappop(hq)
        if cost > distance[now]:
            continue
       
        for next,next_cost in graph[now]:
            if next not in visited:
                if distance[next] > cost + next_cost:
                    distance[next] = cost + next_cost
                    heapq.heappush(hq, (cost+next_cost, next))
    
    return distance

distance = djik(set(), e)

n = s
go_cost = 0
visit = set()
while n != e:
    for next, next_cost in graph[n]:
        if go_cost + next_cost + distance[next] == distance[s]:
            visit.add(next)
            n = next
            go_cost += next_cost
            break

new_distance = djik(visit, e)
result = go_cost + new_distance[s]
print(result)
    
    



    
    
