import sys
input = sys.stdin.readline

def func(x,y):
    if y == 0:
        return x
    return func(y,x%y)

N = int(input())
csgbs = 1
D = [0] * N

graph = [[] for _ in range(N)]
for _ in range(N-1):
    a,b,p,q = map(int, input().split())
    graph[a].append((b,p,q))
    graph[b].append((a,q,p))
    csgbs *= (p*q//func(p, q))
    
visited = [0]*(N)

def dfs(x):
    visited[x]=1
    for to,p,q in graph[x]:
        if not visited[to]:
            D[to] = D[x]*q//p
            dfs(to)
            
            
D[0] = csgbs
dfs(0)
aa = D[0]

for i in range(1,N):
    aa = func(aa, D[i])
    
for i in range(N):
    print(int(D[i]//aa) ,end=' ')

        
    

