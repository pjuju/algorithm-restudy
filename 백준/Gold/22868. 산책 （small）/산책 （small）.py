import sys
from collections import deque
input = sys.stdin.readline

def bfs(start,end,path):
    queue = deque()
    queue.append((start, path))

    while True:
        now, p = queue.popleft()
        for next in graph[now]:
            if next == end:
                return p+[next]
            if next not in p:
                queue.append((next, p+[next]))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A,B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
for i in range(N):
    graph[i].sort() # 사전순이니까

S,E = map(int, input().split())

visited = [0] * (N+1)
visited[S] = True

go_path = bfs(S,E,[S])
entire_path = bfs(E,S,go_path)
# print(go_path)
# print(entire_path)
print(len(entire_path)-1)


