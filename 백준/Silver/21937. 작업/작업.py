import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    # a를 해야 b를 할 수 있음
    graph[b].append(a)
    
cnt = -1
dq = deque()
dq.append(int(input()))
visited = [0] * (N+1)

while dq:
    now = dq.popleft()
    cnt += 1
    
    for next in graph[now]:
        if not visited[next]:
            visited[next] = 1
            dq.append(next)    
            
print(cnt)