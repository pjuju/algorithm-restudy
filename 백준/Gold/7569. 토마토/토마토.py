from collections import deque 

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

tomatoes = deque()

for x in range(H):
    for y in range(N):
        for z in range(M):
            if arr[x][y][z] == 1:
                tomatoes.append((x,y,z))

dx, dy, dz = [1,-1,0,0,0,0], [0,0,1,-1,0,0], [0,0,0,0,1,-1]

while tomatoes:
    x,y,z = tomatoes.popleft()

    for i in range(6):
        nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]

        if 0<=nx<H and 0<=ny<N and 0<=nz<M:
            if arr[nx][ny][nz] == 0:
                arr[nx][ny][nz] = arr[x][y][z] + 1
                tomatoes.append((nx,ny,nz))


result = 0
flag = False
for x in range(H):
    if not flag:
        for y in range(N):
            if not flag:
                for z in range(M):                    
                    if arr[x][y][z] == 0:
                        result = -1
                        flag = True
                        break
                    if arr[x][y][z] > result:
                        result = arr[x][y][z] -1   

print(result)
                