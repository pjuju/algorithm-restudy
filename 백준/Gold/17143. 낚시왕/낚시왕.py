import sys
input = sys.stdin.readline

R,C,M = map(int, input().split())
result = 0

dr, dc = [0,-1,1,0,0], [0,0,0,1,-1]
def shark_move(r,c):    

    s,d,z = arr[r][c]    
    arr[r][c] = 0    
    next_r, next_c = r+dr[d]*s, c+dc[d]*s
    
    while next_r > R-1 or next_r < 0 :                
        if next_r < 0 and d == 1:
            next_r = -next_r
            d = 2
        if next_r > R-1 and d == 2:
            next_r = 2*(R-1)-next_r  
            d = 1  
    
    while next_c > C-1 or next_c < 0 :
        if next_c > C-1 and d == 3:
            next_c = 2*(C-1)-next_c
            d = 4
        if next_c < 0 and d == 4:
            next_c = -next_c
            d = 3           
    
    return next_r, next_c, s, d, z

sharks = []
arr = [[0] * C for _ in range(R)]
for _ in range(M):
    r,c,s,d,z = map(int, input().split())
    # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기
    # d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽    
    sharks.append((r-1,c-1))
    arr[r-1][c-1] = s,d,z
    
# 이동, 낚시
now_c = -1
while now_c < C-1:
    now_c += 1 
     
    # 낚시
    for r in range(R):
        if arr[r][now_c]:   
            result += arr[r][now_c][2]            
            arr[r][now_c] = 0            
            break
          
    next_sharks = []   
    # 상어들 한번에 이동한 결과 
    for r,c in sharks:   
        if arr[r][c]:     
            next_r,next_c,s,d,z = shark_move(r,c)
            next_sharks.append((next_r, next_c, s, d, z))
    
    sharks = []
    for next_r,next_c,s,d,z in next_sharks:     
         
        if not arr[next_r][next_c]:
            sharks.append((next_r,next_c))
            arr[next_r][next_c] = s,d,z

        else:
            if arr[next_r][next_c][2] < z:
                arr[next_r][next_c] = s,d,z

print(result)

    
    
    
    