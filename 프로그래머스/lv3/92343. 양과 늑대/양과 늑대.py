answer = 0


    


def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for s,e in edges:
        graph[s].append(e)
    
    visited = [0] * len(info)
    visited[0] = 1
    
    result = []
    
    def dfs(sheep, wolf):
        if wolf >= sheep:
            return
        result.append(sheep)
        
        for s,e in edges:
            if visited[s] and not visited[e]:
                visited[e] = 1
                if info[e]:
                    dfs(sheep, wolf+1)
                else:
                    dfs(sheep+1, wolf)
                visited[e] = 0
    dfs(1,0)
    
    return max(result)