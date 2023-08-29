import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(input().split()) for _ in range(N)]

dr, dc = [1,0], [0,1]
min_dp = [[1e9] * N for _ in range(N)]
max_dp = [[-1e9] * N for _ in range(N)]
min_dp[0][0] = max_dp[0][0] = int(arr[0][0])


dq = deque()
dq.append((0,0,int(arr[0][0])))

while dq:
    cr, cc, cost = dq.popleft()
    for x in range(2):
        nr, nc = cr+dr[x], cc+dc[x]
        if nr<N and nc<N:
            cal = arr[nr][nc]
            for y in range(2):
                nnr, nnc = nr+dr[y], nc+dc[y]
                if nnr<N and nnc<N:
                    num = int(arr[nnr][nnc])

                    if cal == '-':
                        next_cost = cost - num
                    elif cal == '+':
                        next_cost = cost + num
                    else:
                        next_cost = cost * num
                    
                    if next_cost > max_dp[nnr][nnc]:
                        max_dp[nnr][nnc] = next_cost
                        dq.append((nnr,nnc,next_cost))
                    
                    if next_cost < min_dp[nnr][nnc]:
                        min_dp[nnr][nnc] = next_cost
                        dq.append((nnr,nnc,next_cost))

            
print(max_dp[-1][-1], min_dp[-1][-1])