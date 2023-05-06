import heapq


def solution(n, times):
    
    left = 1
    right = max(times) * n
    
    while left < right:
        mid = (left+right)//2
        people = 0
        for time in times:
            people += (mid // time)
            if people >= n:
                right = mid
                break
        if people < n:
            left = mid+1
    
    return left
        # people이 많으면 시간이 너무 많았음
        # people이 적으면 
    
   