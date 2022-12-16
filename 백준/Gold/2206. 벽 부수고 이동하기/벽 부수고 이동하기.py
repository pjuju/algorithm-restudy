from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

INF = 0xfffff
cnt_arr = [[INF] *M for _ in range(N)]
cnt_arr_check = [[INF] *M for _ in range(N)]
cnt_arr[0][0] = cnt_arr_check[0][0] = 0
dr, dc = [1,-1,0,0], [0,0,1,-1]

queue = deque()
queue.append((0,0,0))

while queue:
    r,c,check = queue.popleft()

    for i in range(4):
        nr,nc = r+dr[i], c+dc[i]

        if 0<=nr<N and 0<=nc<M:
            if check: #이미 벽을 한 번 부쉈으면
                if arr[nr][nc] == 0: #갈 수 있는 벽이면
                    if cnt_arr_check[nr][nc] > cnt_arr_check[r][c] + 1:
                        cnt_arr_check[nr][nc] = cnt_arr_check[r][c] + 1
                        queue.append((nr,nc,1))

            else: #벽을 안 부쉈으면
                
                if arr[nr][nc] == 0: #갈 수 있는 벽이면                    
                    if cnt_arr[nr][nc] > cnt_arr[r][c] + 1:
                        
                        cnt_arr[nr][nc] = cnt_arr[r][c] + 1
                        queue.append((nr,nc,0))

                if arr[nr][nc] == 1: #갈 수 없는 벽이면
                    
                    if cnt_arr_check[nr][nc] > cnt_arr[r][c] + 1:
                        cnt_arr_check[nr][nc] = cnt_arr[r][c] + 1
                        queue.append((nr,nc,1))

result = min(cnt_arr_check[N-1][M-1],cnt_arr[N-1][M-1])
if result == INF:
    print(-1)
else:
    print(result+1)


           


