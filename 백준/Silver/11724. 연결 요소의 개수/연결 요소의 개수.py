import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parents = [i for i in range(N+1)]

def find(x):
    if x == parents[x]:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    if a > b:
        a,b = b,a
    
    pa, pb = find(a), find(b)
    parents[pb] = pa

for _ in range(M):
    a,b = map(int, input().split())
    union(a,b)

_set = set()
for i in range(1, N+1):
    _set.add(find(i))

print(len(_set))
