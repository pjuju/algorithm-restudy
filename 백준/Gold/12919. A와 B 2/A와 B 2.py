from collections import deque

S = input()
T = input()

dq = deque()
dq.append(T)
result = 0
while dq:
    t = dq.popleft()    
    if t == S:
        result = 1
        break
    if len(t) < len(S):        
        break

    if t[-1] == 'A':
        dq.append(t[:-1])
    if t[0] == 'B':    
        dq.append(t[::-1][:-1])

print(result)