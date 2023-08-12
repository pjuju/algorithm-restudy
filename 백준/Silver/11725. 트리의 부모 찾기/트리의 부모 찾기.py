import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
parents = [0] * (N+1)
parents[1] = 1
for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dq = deque()
dq.append(1)
while dq:
    now = dq.popleft()
    for next in graph[now]:
        if not parents[next]:
            parents[next] = now
            dq.append(next)

for i in range(2, N+1):
    print(parents[i])