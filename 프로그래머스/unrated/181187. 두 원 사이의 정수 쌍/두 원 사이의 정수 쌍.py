import math

def solution(r1, r2):
    answer = 0
    for i in range(1,r2+1):
        # y2 = math.floor(math.sqrt(r2**2 - i**2))
        # y1 = math.ceil(math.sqrt(r1**2 - i **2)) if r1 >= i else 0
        y2 = int((r2**2 - i**2)**(1/2))
        y1 = (r1**2 - i**2)**(1/2) if r1 >= i else 0
        if y1%1:
            y1 = int(y1+1)
        answer += (y2-y1+1)
    
    return answer * 4
            