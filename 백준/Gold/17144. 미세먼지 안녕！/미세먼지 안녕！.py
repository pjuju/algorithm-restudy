import sys
input = sys.stdin.readline
from copy import deepcopy

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

air_tr = air_dr = air_c = -1
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            if air_tr == -1:
                air_tr, air_c = i,j
            else:
                air_dr = i

t_dr = [-1,0,1,0]
t_dc = [0,1,0,-1]
                
def air_t():

    d = 0
    r,c = air_tr-1, air_c
    
    while True:
        if r == air_tr and c == air_c+1:
            break
        
        nr, nc = r+t_dr[d], c+t_dc[d]    
        
        if 0<=nr<=air_tr and 0<=nc<C:
            arr[r][c] = arr[nr][nc]
            r, c = nr, nc
        else:
            d += 1

    arr[r][c] = 0


d_dr = [1,0,-1,0]
d_dc = [0,1,0,-1]

def air_d():
    d = 0
    r,c = air_dr+1, air_c
    
    while True:
        if r == air_dr and c == air_c+1:
            break

        nr, nc = r+d_dr[d], c+d_dc[d]    
        if air_dr<=nr<R and 0<=nc<C:
            arr[r][c] = arr[nr][nc]
            r, c = nr, nc
        else:
            d += 1

    arr[r][c] = 0

dr, dc = [0,0,-1,1], [-1,1,0,0]
def move(arr):
    new_arr = deepcopy(arr)
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:                
                for x in range(4):
                    nr, nc = r+dr[x], c+dc[x]
                    if 0<=nr<R and 0<=nc<C and arr[nr][nc] != -1:
                        new_arr[nr][nc] += arr[r][c]//5
                        new_arr[r][c] -= arr[r][c] // 5
                        
    return new_arr

for _ in range(T):
    arr = move(arr)
    air_d()
    air_t()
    
result = 2  
for i in range(R):
    for j in range(C):
        result += arr[i][j]
# print('')
# for x in arr:
#     print(x)
print(result)
      