import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    row_sum = [0] * N
    col_sum = [0] * N
    
    for i in range(N):
        for j in range(N):
            row_sum[i] += arr[i][j]
            col_sum[i] += arr[j][i]
    
    for _ in range(M):
        r1, c1, r2, c2, v = map(int, input().split())
        for r in range(r1-1, r2):
            row_sum[r] += (c2-c1+1)*v
        for c in range(c1-1, c2):
            col_sum[c] += (r2-r1+1)*v
            
    print(*row_sum)
    print(*col_sum)