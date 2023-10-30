import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = [[float('inf')] * (N) for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c

for i in range(N):
    d[i][i] = 0

for p in range(N):
    for a in range(N):
        for b in range(N):
            if d[a][b] > d[a][p] + d[p][b]:
                d[a][b] = d[a][p] + d[p][b]

K = int(input())
lst = list(map(int, input().split()))

result_d = float('inf')
result = []
for i in range(N):
    val = 0
    for k in lst:
        val = max(val, (d[k-1][i] + d[i][k-1]))
    if val == result_d:
        result.append(i+1)
    elif val < result_d:
        result = [i+1]
        result_d = val

print(*result)
