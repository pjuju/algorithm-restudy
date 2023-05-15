from collections import deque

N = int(input())
dq = deque()
for i in range(10):
    dq.append((i,i))

result = -1
cnt = 0
while dq:
    n,x = dq.popleft()
    cnt += 1
    if cnt == N:
        result = n
        break
    for y in range(0,x):
        dq.append((int(str(n) + str(y)),y))
        
print(result)