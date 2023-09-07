import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
from copy import deepcopy

N,M,D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.reverse()

num = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            num += 1

def move():
    cnt = 0
    for c in range(M):
        if temp_arr[0][c]:
            temp_arr[0][c] = 0
            cnt += 1
    for r in range(1, N):
        for c in range(M):
            if temp_arr[r][c]:
                temp_arr[r][c] = 0
                temp_arr[r-1][c] = 1
            
    return cnt        

def func(lst):
    # print(lst)
    delete = 0
    kill = 0
    
    while delete+kill != num:
        kills = set()

        # 각 궁수들이 가장 가까운 적 찾는다
        for x in lst:
            dq = deque()
            dq.append((0,x,1))
            while dq:
                r,c,d = dq.popleft()
                
                if temp_arr[r][c]:       
                    # 만약 적 찾으면 set에 추가
                    kills.add((r,c))
                    break
                if d == D:
                    continue
                for (nr,nc) in ((r,c-1), (r+1,c), (r,c+1)):
                    if 0<=nr<N and 0<=nc<M:
                        dq.append((nr,nc,d+1))
                        
        
        for r,c in kills:
            temp_arr[r][c] = 0
            
        delete += move()
        kill += len(kills)
                
    return kill


result = 0
for comb in combinations(range(M), 3):
    temp_arr = deepcopy(arr)

    result = max(result, func(comb))
print(result)
