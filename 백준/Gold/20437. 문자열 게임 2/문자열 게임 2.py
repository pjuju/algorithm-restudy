T = int(input())
for _ in range(T):
    W = list(input())
    K = int(input())

    dd = dict()
    for i in range(len(W)):
        t = W[i]
        if t not in dd:
            dd[t] = [i]
        else:
            dd[t].append(i)
    
    max_val = 0 
    min_val = 10000
    for t in dd:
        lst = dd[t]
        if len(lst) >= K: # 3개 0 3 - 3 + 1 0
            for i in range(len(lst)-K+1):
                val = lst[i+K-1]-lst[i] + 1
                max_val = max(max_val, val)
                min_val = min(min_val, val)
    
    if max_val:
        print(min_val,max_val)
    else:
        print(-1)


        