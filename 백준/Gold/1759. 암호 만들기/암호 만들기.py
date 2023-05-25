from collections import deque

L,C = map(int, input().split())
lst = sorted(input().split())

dq = deque()
dq.append(('', -1))

while dq:
    text, idx = dq.popleft()
        
    if len(text) == L:
        a,b = 0,0
        for t in text:
            if t in ['a','e','i','o','u']:
                a += 1
            else:
                b += 1
                
        if a > 0 and b > 1:
            print(''.join(text))
        continue
    
    for i in range(idx+1, C-L+len(text)+1):
        dq.append((text+lst[i], i))
    
    
    
    