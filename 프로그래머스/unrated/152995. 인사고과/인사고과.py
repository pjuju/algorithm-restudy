def solution(scores):
    answer = 1    
    val = sum(scores[0])
    arr = sorted(scores,key=lambda x:(-x[0],x[1]))
    
    max_y = arr[0][1]
    for p in arr:
        if p[1] < max_y:
            if p == scores[0]:
                return -1
        else:
            max_y = p[1]
            if sum(p) > val:
                answer += 1
    
    return answer