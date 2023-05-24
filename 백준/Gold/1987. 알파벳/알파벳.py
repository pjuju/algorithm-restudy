import sys

dr, dc = [0,0,1,-1], [1,-1,0,0]
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

r,c = 0,0
result = 0
q = set()
q.add((r,c,arr[r][c]))
while q:    
    r, c, text = q.pop()    
    result = max(len(text), result)
    for x in range(4):
        nr, nc = r+dr[x], c+dc[x]
        if 0<=nr<R and 0<=nc<C:
            if not arr[nr][nc] in text:              
                q.add((nr,nc,text+arr[nr][nc]))
                
print(result)

