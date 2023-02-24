import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] *(N+1)
cnt = [0] *(N+1)

for _ in range(M):
    A,B = map(int, input().split())
    graph[B].append(A)

for i in range(N+1):
    visited = [0] * (N+1)
    visited[i] = 1
    queue = deque([i])
    
    while queue:
        now = queue.popleft()
        cnt[i] += 1
        for next in graph[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = 1
                
max_cnt = 0
results = []
for i in range(N+1):
    if cnt[i] > max_cnt:
        max_cnt = cnt[i]
        results = [i]
    
    elif cnt[i] == max_cnt:
        results.append(i)
        
print(*results)