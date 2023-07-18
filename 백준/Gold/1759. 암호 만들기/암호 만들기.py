import sys
input = sys.stdin.readline

L, C = map(int, input().split())
lst = list(input().split())

lst.sort()

def dfs(text,x,a,b):
    if a+b+C-x-1 < L:
        return
    if len(text) == L:
        if a >= 1 and b >= 2:
            print(text) 
            return
    for i in range(x+1, C):
        if lst[i] in 'aeiou':
            dfs(text+lst[i],i,a+1,b)
        else:
            dfs(text+lst[i],i,a,b+1)  
            
dfs('',-1,0,0)  
    