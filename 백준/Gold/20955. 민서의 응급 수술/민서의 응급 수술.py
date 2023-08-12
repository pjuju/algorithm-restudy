import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parents = [i for i in range(1+N)]

def find(x):
    if x == parents[x]:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    px, py = find(x), find(y)
    if px < py:
        parents[py] = px
    elif py < px:
        parents[px] = py

graph = [[] for _ in range(N+1)]

result = 0
for _ in range(M):
    a,b = map(int, input().split())
    if find(a) == find(b):
        result += 1
    else:
        union(a,b)

for i in range(2, N+1):
    if find(i-1) != find(i):
        union(i-1, i)
        result += 1

print(result)