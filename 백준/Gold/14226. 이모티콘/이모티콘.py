from collections import deque
from collections import defaultdict

S = int(input())
dq = deque()
dq.append((1,0,0))
visited = defaultdict(int)
visited[(1,0)] = 0

while dq:
    x,c,cnt = dq.popleft()
    if x == S:
        print(cnt)
        break
    
    if (x,x) not in visited:
        dq.append((x,x,cnt+1))
        visited[(x,x)] = cnt+1
    if x > 0 and (x-1,c) not in visited:
        dq.append((x-1,c,cnt+1))
        visited[(x-1,c)] = cnt+1
    if (x+c, c) not in visited:
        dq.append((x+c, c, cnt+1))
        visited[(x+c,c)] = cnt+1
