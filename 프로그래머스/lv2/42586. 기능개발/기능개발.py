import math 
from collections import deque
def solution(progresses, speeds):
    
    dq = deque()
    cnt = 0
    
    for i in range(len(progresses)):
        dq.append((progresses[i], speeds[i]))
    
    answer = []
    while dq:
        p,s = dq.popleft()
        cnt = math.ceil((100-p)/s)
        ans = 1
        while dq:
            np,ns = dq[0]
            if np + ns*cnt >= 100:
                dq.popleft()
                ans += 1
            else:
                break
        answer.append(ans)
                
    return answer