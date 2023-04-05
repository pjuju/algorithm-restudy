from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        sorted_candidates = Counter(candidates).most_common()
        
        for m,c in sorted_candidates:
            if c <= 1 or c != sorted_candidates[0][1]:
                break
            answer.append(m)
     
    return sorted(answer)