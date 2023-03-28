def solution(s):
    answer = True
    
    queue = []
    for a in s:
        if a == '(':
            queue.append(a)
        else:
            if not queue:
                return False
            queue.pop()
            
    if queue:
        return False
                
    return True