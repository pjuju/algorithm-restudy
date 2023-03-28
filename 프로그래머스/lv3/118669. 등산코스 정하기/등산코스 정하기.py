import heapq

def solution(n, paths, gates, summits):
    
    edges = [[] for _ in range(n+1)]
    
    for s,e,v in paths:
        edges[s].append((e,v))
        edges[e].append((s,v))
    
    distance = [0xffffff] * (n+1)
    hq = []
    for gate in gates:
        heapq.heappush(hq, (0,gate)) 
        distance[gate] = 0    
        
    answer = 0xfffffff
    answer_summit = False
    while hq:
        cost, now = heapq.heappop(hq)
        if cost > answer:
            break
        if now in summits:
            if cost < answer:
                answer = cost
                answer_summit = now
            if cost == answer:
                answer_summit = min(now, answer_summit)
            continue
        for next, val in edges[now]:
            d = max(cost, val)
            if d < distance[next]:
                distance[next] = d
                heapq.heappush(hq, (d,next))
    
    return answer_summit, answer
