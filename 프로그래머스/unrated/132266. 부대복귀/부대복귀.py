import heapq
import sys
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    
    start = destination
    INF = sys.maxsize
    distance = [INF] * (n+1)
    
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (0,start))
    # print(queue)
    # print(graph)
    
    while queue:
        cost, now = heapq.heappop(queue)
        # print(cost,now)
        for next in graph[now]:
            # print(next)
            if distance[next] > cost + 1:
                distance[next] = cost + 1
                heapq.heappush(queue, (cost+1,next))
    
    
    for a in sources:
        if distance[a] == INF:
            answer.append(-1)
        else:
            answer.append(distance[a])
    return answer