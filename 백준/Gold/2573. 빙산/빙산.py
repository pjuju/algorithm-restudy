from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr, dc = [0,0,-1,1], [1,-1,0,0]
ice = []

for r in range(N):
    for c in range(M):
        if arr[r][c]:
            ice.append((r,c))
    
def check():    
    visited = [[0] * M for _ in range(N)]
    dq = deque()
    fr, fc = ice[0]
    dq.append((fr,fc))
    visited[fr][fc] = 1
    
    cnt = 0
    while dq:
        r, c = dq.popleft()
        cnt += 1
        for x in range(4):
            nr, nc = r+dr[x], c+dc[x]
            if 0<=nr<N and 0<=nc<M:
                if not visited[nr][nc] and arr[nr][nc]:
                    visited[nr][nc] = 1
                    dq.append((nr,nc))

    if cnt < len(ice):
        return True
    
    return False


result = 0
time = 0
while ice:
    # print(time)
    # for a in arr:
    #     print(a)

    if check():
        result = time
        break

    time += 1
    
    cnt = [[0] * M for _ in range(N)]
    for r,c in ice:
        flag = True        
        for x in range(4):
            nr, nc = r+dr[x], c+dc[x]
            if not arr[nr][nc]:
                cnt[r][c] += 1                

    new_ice = []
    for r,c in ice:
        if cnt[r][c] >= arr[r][c]:
            arr[r][c] = 0
        else:
            arr[r][c] -= cnt[r][c]
            new_ice.append((r,c))
    
    ice = new_ice

print(result)