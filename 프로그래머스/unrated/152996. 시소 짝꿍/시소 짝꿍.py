def solution(weights):
    answer = 0
    max_w = max(weights)
    cnt = [0] * (max_w+1)
    for w in weights:        
        if cnt[w]:
            answer += cnt[w]            
        cnt[w] += 1
            
    for w in weights:
        for a in (w*2, w*3/2, w*4/3):
            if a == int(a) and a <= max_w :
                if cnt[int(a)]:
                    answer += cnt[int(a)]
    return answer
        