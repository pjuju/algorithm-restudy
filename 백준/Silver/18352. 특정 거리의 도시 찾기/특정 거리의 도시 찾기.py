import sys
input = sys.stdin.readline
from collections import deque

N,M,K,X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int, input().split())
    graph[A].append(B)

queue = deque()
queue.append((X,0))
visited = [0] * (N+1)
visited[X] = True
result = []

while queue:
    now, cnt = queue.popleft()    
    if cnt == K:
        result.append(now)
        continue
    
    for next in graph[now]:
        if not visited[next]:
            queue.append((next, cnt+1))
            visited[next] = True
            

if result:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)