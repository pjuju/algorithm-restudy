import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n+1)]

def union(a,b):
    pa, pb = find(a), find(b)
    parents[pb] = parents[pa]
    

def find(a):
    if parents[a] == a:
        return a
    
    parents[a] = find(parents[a])
    return parents[a]



for _ in range(m):
    x,a,b = map(int, input().split())
    if x == 0: # 합집합 (유니온)
        union(a,b)
    if x == 1: # 부모 같은지 확인 (파인드)
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')