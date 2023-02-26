import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# n+1개의 집합 {0}, {1}, {2}, ,,, , {n}
# 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산 수행
def union(x,y):    
    a = find(x) 
    b = find(y)
    belongs[b] = a

def find(x):
    if x == belongs[x]:
        return belongs[x]
    
    if x != belongs[x]:
        belongs[x] = find(belongs[x])
        return belongs[x]
    
belongs = [x for x in range(n+1)]
for _ in range(m):
    x, a, b = map(int, input().split())
    
    if x == 0:
        union(max((a,b)),min((a,b)))
    
    if x == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')


