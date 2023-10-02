import sys
input = sys.stdin.readline

N = int(input())
lst = [0]
for _ in range(N):
    lst.append(int(input()))

def func(x):
    visited = set()
    y = x
    while True:
        y = lst[y]
        if y in visited:
            return
        
        visited.add(y)
        if y == x:
            _set.update(visited)
            return
        

_set = set()
for i in range(1, N+1):
    func(i)

result = []
for x in _set:
    result.append(x)

result.sort()
print(len(result))
for x in result:
    print(x)