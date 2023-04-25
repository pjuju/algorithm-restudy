from collections import deque 
import sys
sys.setrecursionlimit(10**6)




def solution(n, lighthouse):
    graph = [[] for _ in range(n+1)]    
    for a,b in lighthouse:        
        graph[a].append(b)
        graph[b].append(a)    
   
    visited = [0] * (n+1)
    visited[1] = 1  
    
    result = 0
    def func(x):
        nonlocal result
        a = 0
        b = 0
        for y in graph[x]:
            if not visited[y]:
                visited[y] = 1
                val = func(y)
                if val != -1:
                    a += 1
                    b += val
        if a>b:
            result += 1
            return -1
        else:
            result += b
            return a
                
    
    func(1)
    return result
