import heapq


def solution(k, n, reqs):
    answer = 1e9
    
    lst = [[] for _ in range(k+1)]
    for a,b,c in reqs:
        lst[c].append((a,b))

    def solv():
        val = 0
        for i in range(1, k+1):
            hq = []
            for _ in range(cnt[i]):
                heapq.heappush(hq, (0))
            for start, time in lst[i]:                
                f_time = heapq.heappop(hq)
                if f_time > start:
                    val += f_time - start
                    start = f_time                    
                heapq.heappush(hq, start+time)
                
        return val

    cnt = [1] * (k+1)
  
    def func(i, c):
        nonlocal answer
        if c == n-k:
            answer = min(answer,solv())            
            return
        
        for j in range(i, k+1):
            cnt[j] += 1
            func(j, c+1)  
            cnt[j] -= 1
        
    func(1, 0)

    return answer