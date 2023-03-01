import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
times = [0] * (N+1)
cnt = [0] * (N+1)
graph = [[] for i in range(N+1)]
pre_graph = [[]]
for i in range(1,N+1):
    arr = list(map(int, input().split()))[:-1]
    time = arr.pop(0)
    times[i] = time
    pre_graph.append(arr)
    for x in arr:
        # print(arr, x, i)
        graph[x].append(i)
        cnt[i] += 1

results = [0] * (N+1)
queue = deque()
for x in range(1, N+1):
    if cnt[x] == 0:
        queue.append(x)

# print(graph)
while queue:
    now = queue.popleft()
    max_pre = 0
    for x in graph[now]:
        cnt[x] -= 1
        if cnt[x] == 0:
            queue.append(x)
    for y in pre_graph[now]:
        if results[y] > max_pre:
            max_pre = results[y]
    result = max_pre + times[now]
    results[now] = result

results.pop(0)
for result in results:
    print(result)      
