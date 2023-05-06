from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for s,e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    times = [0] * (n+1)
    visited = [0] * (n+1)
    visited[1] = 1
    dq = deque()
    dq.append(1)
    
    while dq:
        now = dq.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = 1
                times[next] = times[now] + 1
                dq.append(next)
    
    return times.count(max(times))