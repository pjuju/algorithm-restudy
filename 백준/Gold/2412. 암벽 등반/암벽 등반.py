import sys
input = sys.stdin.readline
from collections import deque

n,t = map(int, input().split())

go = set()

for _ in range(n):
    x,y = map(int, input().split())
    go.add((x,y))

dq = deque()
dq.append((0,0,0))

result = -1
while dq:
    x,y,c = dq.popleft()
    
    if y == t:
        result = c
        break
    
    for ny in range(y-2,y+3):
        for nx in range(x-2, x+3):
            if (nx,ny) in go:
                dq.append((nx,ny,c+1))
                go.remove((nx,ny))
                
print(result)
    
