import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
distance = [[float('inf')] * (n) for _ in range(n)]

for i in range(n):
    distance[i][i] = 0

for _ in range(r):
    a,b,c = map(int, input().split())
    distance[a-1][b-1] = c
    distance[b-1][a-1] = c

for a in range(n):
    for x in range(n):
        for y in range(n):
            distance[x][y] = min(distance[x][a] + distance[a][y], distance[x][y])

result = 0
for i in range(n):
    cnt = 0
    for j in range(n):        
        if distance[i][j] <= m:
            cnt += items[j]
    result = max(result, cnt)

print(result)



