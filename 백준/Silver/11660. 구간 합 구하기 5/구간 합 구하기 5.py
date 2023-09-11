import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0]* (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
sub_sum = [[0] * (N+1) for _ in range(N+1)]

for r in range(1, N+1):
    for c in range(1, N+1):
        sub_sum[r][c] = sub_sum[r-1][c] + sub_sum[r][c-1] - sub_sum[r-1][c-1] + arr[r][c]

for _ in range(M):
    r1, c1, r2, c2 = map(int, input().split())
    result = sub_sum[r2][c2] - sub_sum[r1-1][c2] - sub_sum[r2][c1-1] + sub_sum[r1-1][c1-1]
    print(result)

