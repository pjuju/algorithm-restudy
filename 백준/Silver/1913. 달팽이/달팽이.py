N = int(input())
X = int(input())
arr = [[0] * N for _ in range(N)]
start=nr=nc=N//2
num = 1
result = N//2+1, N//2+1
arr[start][start] = num


dr, dc = [-1,1,0,0],[0,0,1,-1] # 위 아래 오른쪽 왼쪽
direction = 0
while num < N**2:
    if nr+nc == 2*start: #아래,위
        if nc>start: #
            direction = 1
        else:
            direction = 0
    
    elif nc-1 == nr:
        if nr < start:
            direction = 2
    elif nr == nc and nr > start:
        direction = 3
    
    nr, nc = nr + dr[direction], nc + dc[direction]
    
    num += 1
    arr[nr][nc] = num

    if num == X:
        result = nr+1,nc+1
        
for a in arr:
    print(*a)
print(*result)