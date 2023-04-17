import heapq

def solution(targets):
    hq = []
    for a,b in targets:
        heapq.heappush(hq, (a,b))
        
    answer = 0
    end = -1
    while hq:
        a,b = heapq.heappop(hq)
        if a >= end:            
            answer += 1
            end = b
        if b < end:
            end = b
        
            
    return answer