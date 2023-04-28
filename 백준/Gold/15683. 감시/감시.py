import copy
dr, dc = [-1,1,0,0], [0,0,-1,1] # 상화좌우 (0,1,2,3)
directions = [[], 
            [[0],[1],[2],[3]], # 1번 CCTV
            [[0,1],[2,3]], # 2번 CCTV
            [[0,3],[3,1],[1,2],[2,0]], # 3번 CCTV
            [[0,1,2],[0,2,3],[0,1,3],[1,2,3]], # 4번 CCTV
            [[0,1,2,3]] # 5번 CCTV
            ] 

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            cctvs.append((i,j,arr[i][j]))


        
result = 0xffffffffffff
def func(i, arr):
    global result
    if i == len(cctvs):
        cnt = 0
        for a in range(N):
            for b in range(M):
                if not arr[a][b]:
                    cnt += 1 
        result = min(cnt, result)
        
        return
    
    sr,sc,n = cctvs[i] # cctv 위치
    for dircetion in directions[n]: # cctv에 따른 방향 경우
        temp_arr = copy.deepcopy(arr) 
        
        r,c = sr,sc
        for d in dircetion: # 방향 경우들에 따른 방향
            nr, nc = r+dr[d], c+dc[d]
            while 0<=nr<N and 0<=nc<M:
                if temp_arr[nr][nc] == 6:
                    break
                elif temp_arr[nr][nc] == 0:
                    temp_arr[nr][nc] = 7
                nr, nc = nr+dr[d], nc+dc[d]
        func(i+1, temp_arr)

func(0,arr)
print(result)
            
            


            