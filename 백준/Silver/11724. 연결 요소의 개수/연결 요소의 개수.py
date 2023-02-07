N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
result = 0

for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
def dfs(node):
    for next in graph[node]:
        if not visited[next]:
            visited[next] = 1
            dfs(next)
            
for i in range(1, N+1):
    if not visited[i]:
        visited[i] = 1
        result += 1
        dfs(i)
        
print(result)