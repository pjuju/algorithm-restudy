from collections import deque

def solution(queue1, queue2):
    answer = -1
    val = (sum(queue1) + sum(queue2))
    if val %2:        
        return answer
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = (len(queue1) + len(queue2)) * 2
    s_queue1 = sum(queue1)
    s_queue2 = sum(queue2)
    cnt = 0
    
    while cnt < limit:
        # print(queue1, queue2)
        if s_queue1 == val//2:
            answer = cnt
            break 
        
        if queue1 and s_queue1 > s_queue2:
            v = queue1.popleft()
            queue2.append(v)
            s_queue1 -= v
            s_queue2 += v
        elif queue2 and s_queue2 > s_queue1:
            v = queue2.popleft()
            queue1.append(v)
            s_queue2 -= v
            s_queue1 += v
            
        cnt += 1

    
    return answer