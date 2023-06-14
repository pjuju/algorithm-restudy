import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
visited = [0] * (N+1)
mxc = 0
mnc = 0

parents = [i for i in range(N+1)]
def find(a):
    if parents[a] == a:
        return a
    
    parents[a] = find(parents[a])
    return parents[a]

def union(a,b):    
    a, b = find(a), find(b)
    parents[max(a,b)] = parents[min(a,b)]
    
for _ in range(M):
    a,b,c = map(int, input().split())
    mxc += c
    graph.append((c,a,b))

cnt = 0
graph.sort()
for c,a,b in graph:
    if find(a) != find(b):
        union(a,b)
        mnc += c
        cnt += 1
tmp = 0
for i in range(1, N+1):
    if parents[i] == i:
        tmp += 1
 
if tmp >= 2:
    print(-1)
else:
    result = mxc-mnc

    print(result)
