def solution(plans):
    answer = []
    queue = []
    plans.sort(key=lambda x:x[1])
    print(plans)
    for i in range(len(plans)-1):
        name = plans[i][0]
        now = 60 * int(plans[i][1][:2]) + int(plans[i][1][3:])
        cost = int(plans[i][2])        
        next = 60 * int(plans[i+1][1][:2]) + int(plans[i+1][1][3:])        
        x = next-now-cost       
        if x < 0:
            queue.append((name,-x))
        else:
            answer.append(name)
            while x>0 and queue:
                n,c = queue.pop()
                x -= c
                if x >= 0:
                    answer.append(n)
                else:
                    queue.append((n,-x))
        

    answer.append(plans[-1][0])
    while queue:
        answer.append(queue.pop()[0])
        
    return answer