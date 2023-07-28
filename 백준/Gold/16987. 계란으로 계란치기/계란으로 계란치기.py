N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
result = 0 

def dfs(x):    
    global result    
    if x == N:
        cnt = 0
        for i in range(N):
            if lst[i][0] <= 0 :
                cnt += 1
        result = max(cnt, result)
        return
    
    if lst[x][0] <= 0:
        dfs(x+1)
    else:    
        check = False
        for i in range(N):
            if x != i and lst[i][0] > 0:
                check = True
                lst[x][0] -= lst[i][1]
                lst[i][0] -= lst[x][1]                
                dfs(x+1)
                lst[x][0] += lst[i][1]
                lst[i][0] += lst[x][1]
        if not check:
            dfs(x+1)    
dfs(0)

print(result)