import sys
input = sys.stdin.readline
from collections import deque
V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V):
    arr = list(map(int,input().split()))
    for i in range(1,len(arr)-1,2):
        tree[arr[0]].append((arr[i],arr[i+1]))

num = 0
result = 0
visited = [0] * (V+1)

def dfs(i,n):
    visited[i] = 1
    
    global result
    global num

    if n > result:
        result = n
        num = i
    for x,y in tree[i]:
        if not visited[x]:
            dfs(x,n+y)
            visited[x] = 0


dfs(1,0)
visited = [0] * (V+1)
dfs(num,0)

print(result)





