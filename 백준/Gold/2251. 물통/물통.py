import sys
input = sys.stdin.readline
from collections import deque

def give(x,y,to):
    y = x+y
    x = 0
    if y > to:
        x += (y-to)
        y = to
    return x,y


A,B,C = map(int, input().split())
queue = deque()
queue.append((0,0,C))
result = []
check = [(0,0,C)]
while queue:
    a,b,c = queue.popleft()    
    if a == 0:
        result.append(c)    
    # a
    if a:
        # b로
        a1,b1 = give(a,b,B)
        if (a1,b1,c) not in check:
            check.append((a1,b1,c))
            queue.append((a1,b1,c))        
        # c로
        a2,c2 = give(a,c,C)
        if (a2,b,c2) not in check:
            check.append((a2,b,c2))
            queue.append((a2,b,c2))        
    if b:
        # a로
        b3,a3 = give(b,a,A)
        if (a3,b3,c) not in check:
            check.append((a3,b3,c))
            queue.append((a3,b3,c))        
        # c로
        b4,c4 = give(b,c,C)
        if (a,b4,c4) not in check:
            check.append((a,b4,c4))
            queue.append((a,b4,c4))
    if c:
        # a로
        c5,a5 = give(c,a,A)
        if (a5,b,c5) not in check:
            check.append((a5,b,c5))
            queue.append((a5,b,c5))        
        # b로
        c6,b6 = give(c,b,B)
        if (a,b6,c6) not in check:
            check.append((a,b6,c6))
            queue.append((a,b6,c6))
print(*sorted(result))
    
        
        
        



    

