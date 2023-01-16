from collections import deque

T = int(input())
for tc in range(T):
    N,M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (N+1)
    visited[1] = 1

    result = 0
    stack = deque([1])
    while stack:
        a = stack.popleft()
        for b in graph[a]:
            if not visited[b]:
                visited[b] = 1
                result += 1
                stack.append(b)

    print(result)


