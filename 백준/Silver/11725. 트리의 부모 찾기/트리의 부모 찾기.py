N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = [0] * (N+1)
queue = [1]
while queue:
    a = queue.pop(0)
    for i in graph[a]:
        if i in graph[a] and not parents[i]:
            queue.append(i)
            parents[i] = a

for i in range(2,len(parents)):
    print(parents[i])
