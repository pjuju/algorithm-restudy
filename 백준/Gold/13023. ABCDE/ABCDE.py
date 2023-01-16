def dfs(i, cnt):
    global result
        
    visited[i] = 1
    
    if cnt == 5:
        result = 1
        return
    
    for x in graph[i]:
        if not visited[x]:
            dfs(x, cnt+1)
            visited[x] = 0

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

result = 0

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    visited = [0] * N
    dfs(i, 1)
            
print(result)