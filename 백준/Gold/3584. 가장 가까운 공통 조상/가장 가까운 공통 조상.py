T = int(input())

for tc in range(T):    
    N = int(input())
    parents= [0] * (N + 1)
    for _ in range(N-1):
        a,b = map(int, input().split())
        parents[b] = a
    
    x,y = map(int, input().split())
    x_lst = [x]   
    y_lst = [y]
     
    while parents[x]:                
        x_lst.append(parents[x])
        x = parents[x]
    
    while parents[y]:                
        y_lst.append(parents[y])
        y = parents[y]
    
    x_level = len(x_lst) - 1
    y_level = len(y_lst) - 1

    while x_lst[x_level] ==  y_lst[y_level]:
        x_level -= 1
        y_level -= 1
    
    print(x_lst[x_level+1])