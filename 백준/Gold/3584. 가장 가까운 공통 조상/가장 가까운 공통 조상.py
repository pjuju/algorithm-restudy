T = int(input())

for tc in range(T):    
    N = int(input())
    parents = [i for i in range(N+1)]
    for _ in range(N-1):
        a,b = map(int, input().split())
        parents[b] = a
    
    x,y = map(int, input().split())
    x_lst = [x]    
    while True:        
        if x == parents[x]:
            break
        
        x_lst.append(parents[x])
        x = parents[x]
    
    while True:       
        if y in x_lst:
            print(y)
            break
        
        y = parents[y]