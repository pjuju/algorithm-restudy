import sys
from collections import deque
input = sys.stdin.readline
dr, dc = [1,-1,0,0,1,-1,1,-1], [0,0,1,-1,1,-1,-1,1]
N,M,K = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
target = [input().rstrip() for _ in range(K)]


def func(target):
    dq = deque()
    for r in range(N):
        for c in range(M):
            if arr[r][c] == target[0]:
                dq.append((r,c,0))
                
    result = 0
    while dq:
        r,c,idx = dq.popleft()
        if idx == len(target)-1:
            result += 1
            continue
        
        for x in range(8):
            nr, nc = r+dr[x], c+dc[x]
            if nr >= N:
                nr = 0
            elif nr < 0:
                nr = N-1
            if nc >= M:
                nc = 0
            elif nc < 0:
                nc = M-1
            
            if arr[nr][nc] == target[idx+1]:
                dq.append((nr,nc,idx+1))
        
        # for x in range(4,8):
        #     nr, nc = r+dr[x], c+dc[x]
        #     if not (0<=nr<N) and not (0<=nc<M):
        #         if nr < 0 and nc < 0:
        #             nr, nc = N-1, M-1
        #         elif nr < 0 and nc >= M:
        #             nr, nc = N-1, 0
        #         elif nr >= N and nc < 0:
        #             nr, nc = 0, M-1
        #         elif nr >= N and nc >= M:
        #             nr, nc = 0,0
        #     if 0<=nr<N and 0<=nc<M:
        #         if arr[nr][nc] == target[idx]:
        #             dq.append((nr,nc,idx+1))

    return result
    
answer = dict()
for t in target:
    if t not in answer:
        answer[t] = func(t)
    print(answer[t])