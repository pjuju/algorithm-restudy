import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, R = map(int, input().split())
graph = [dict() for _ in range(N+1)]

for _ in range(N-1):
    a,b,d = map(int, input().split())    
    graph[a][b] = d
    graph[b][a] = d

stack = deque([R])
giga_len = 0
giga_node = R

# 기가노드
while stack:
    now = stack.pop()   
    giga_node = now     
    if len(graph[now]) > 1:        
        break
    
    for next, distance in graph[now].items():
        del graph[next][now]        
        stack.append(next)
        giga_len += distance

# 가지노드
def dfs(node,sum_val):
    global gaji_len

    if sum_val > gaji_len:
        gaji_len = sum_val
        
    for next, distance in graph[node].items():        
        del graph[next][node]     
        dfs(next, sum_val+distance)
    
gaji_len = 0
dfs(giga_node, 0)

print(giga_len, gaji_len)
        
