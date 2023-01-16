import sys
read = sys.stdin.readline
from collections import deque

def dfs(V):
    visited[V] = 1
    result.append(V)
    for i in range(N+1):
        if not visited[i] and arr[V][i]:
            dfs(i)

def bfs(V):
    queue.append(V)
    visited[V] = 1
    while queue:
        a = queue.popleft()
        result.append(a)
        for i in range(N+1):
            if not visited[i] and arr[a][i]:
                queue.append(i)
                visited[i] = 1


N, M, V = map(int, read().split())
nodes = [list(map(int, read().split())) for _ in range(M)]

# dfs
visited = [0] * (N+1)
arr = [[0] * (N+1) for _ in range(N+1)]
result = []
for node in nodes:
    arr[node[0]][node[1]] = 1
    arr[node[1]][node[0]] = 1
dfs(V)
print(*result)

# bfs
queue = deque()
visited = [0] * (N+1)
result = []
arr = [[0] * (N+1) for _ in range(N+1)]
for node in nodes:
    arr[node[0]][node[1]] = 1
    arr[node[1]][node[0]] = 1
bfs(V)
print(*result)
