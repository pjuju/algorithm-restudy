import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
M = int(read())
nodes = [list(map(int, read().split())) for _ in range(M)]
arr = [[0] * (N+1) for _ in range(N+1)]
for node in nodes:
    arr[node[0]][node[1]] = 1
    arr[node[1]][node[0]] = 1
visited = [0] * (N+1)

visited[1] = 1
queue = deque([1])
count = 0

while queue:
    a = queue.popleft()
    for i in range(N+1):
        if not visited[i] and arr[a][i] == 1:
            queue.append(i)
            visited[i] = 1
            count += 1
print(count)
