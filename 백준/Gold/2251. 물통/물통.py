from collections import deque
visited = [[0]*(201) for _ in range(201)]
A,B,C = map(int, input().split())
dq = deque()
dq.append((0,0,C))
result = []
while dq:
    a,b,c = dq.popleft()
    if visited[a][b]:
        continue
    visited[a][b] = 1
    # print(a,b,c)
    if a:
        if a+b > B:            
            dq.append((a+b-B,B,c))
        else:
            dq.append((0,a+b,c))
        if a+c > C:
            dq.append((a+c-C,b,C))
        else:
            dq.append((0,b,a+c))
    else:                
        result.append(c)
        
    if b:
        if b+a > A:            
            dq.append((A,a+b-A,c))
        else:
            dq.append((a+b,0,c))
        if b+c > C:
            dq.append((a,b+c-C,C))
        else:
            dq.append((a,0,b+c))
    
    if c:
        if c+a > A:            
            dq.append((A,b,c+a-A))
        else:
            dq.append((a+c,b,0))
        if c+b > B:
            dq.append((a,B,b+c-B))
        else:
            dq.append((a,b+c,0))
            
print(*sorted(result))