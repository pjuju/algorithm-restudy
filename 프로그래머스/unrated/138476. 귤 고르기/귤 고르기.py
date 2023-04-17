from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine).most_common()
    cnt = 0
    answer = 0
    
    for val, c in counter:
        cnt += c
        answer += 1
        if cnt >= k:
            break
    
    return answer