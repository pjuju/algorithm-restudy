T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    color = [0] * (V+1)
    
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = 'YES'
    for i in range(1, V+1):
        if not color[i] and result == 'YES':
            color[i] = 1
            queue = [i]
            while queue and result == 'YES':
                ni = queue.pop(0)
                for l in graph[ni]:
                    if not color[l]:
                        color[l] = -color[ni]
                        queue.append(l)
                    elif color[l] == color[ni]:
                        result = 'NO'
                        break

    print(result)

