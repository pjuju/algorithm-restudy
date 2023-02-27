import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
M = int(input())

adj = []
graph = [[] for _ in range(N)]
for i in range(N):
    i_adj = list(map(int, input().split()))
    
    for j in range(i+1, N):
        if i_adj[j]:
            graph[j].append(i)
            graph[i].append(j)
parents = [i for i in range(N)]
plan = list(map(int, input().split()))

# 다음 거치는 곳의 조상노드가 가야할 곳의 조상노드와 같으면 go

def union(a,b):
    x = find(a)
    y = find(b)
    parents[y] = parents[x] 
    
def find(a):
    # print(a)
    if a == parents[a]:
        return a
    
    parents[a] = find(parents[a])
    return parents[a]


for i in range(N):
    for j in graph[i]:
        if i > j:
            union(i,j)
            
            
for i in range(len(plan)):
    plan[i] -= 1

result = 'YES'  
parent = find(plan[0])

for x in plan:
    if find(x) != parent:
        result = 'NO'
        break

print(result)



