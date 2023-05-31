from collections import deque
N = int(input())
lst = list(map(int, input().split()))

dq = deque()    
dq.append((0,0))

answer = []
for i in range(N):
    ans = 0
    while dq:
        val, idx = dq.pop()
        
        if val > lst[i]:
            ans = idx
            dq.append((val,idx))
            break
    answer.append(ans)
    dq.append((lst[i], i+1))

print(*answer)
        
        
        