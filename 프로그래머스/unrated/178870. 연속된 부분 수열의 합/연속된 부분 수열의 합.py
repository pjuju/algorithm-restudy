def solution(sequence, k):
    answer = []
    n = len(sequence)
    limit_sum, end = 0,0
    
    for i in range(len(sequence)):
        while limit_sum < k and end < n:
            limit_sum += sequence[end]
            end +=1
            
        if limit_sum == k:
            answer.append([i, end-1, end-1-i])
        
        limit_sum-= sequence[i]
        
    answer = sorted(answer, key=lambda x: x[2])
    
    return answer[0][:2]