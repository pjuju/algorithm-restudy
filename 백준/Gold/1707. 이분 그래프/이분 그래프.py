import sys
input = sys.stdin.readline
from collections import deque

# 그래프의 정점을 둘로 분할, 각 집합에 속한 정점끼리는 서로 인접하지 않는다 = 이분 그래프
# def bfs(i):


T = int(input())
for _ in range(T):
    V, E = map(int ,input().split())
    
    graph = [[] for _ in range(V+1)]
    
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    graph_sep = [0] * (V+1)

    result = 'YES'
    for i in range(1, V+1):
        if (result == 'YES') and (not graph_sep[i]):
            
            queue = deque()
            graph_sep[i] = 1
            queue.append(i)

            while queue:
                now = queue.popleft()
                color = graph_sep[now]
                for next in graph[now]:                    
                    if not graph_sep[next]:
                        graph_sep[next] = -color
                        queue.append(next)
                    
                    elif graph_sep[next] == color:
                        result = "NO"
                        break
                        
    print(result)