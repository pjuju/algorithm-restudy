n = int(input())
m = int(input())
INF = 0xffffff
distance = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    if distance[a][b] > c:
        distance[a][b] = c


for i in range(1, n+1): # 징검다리
    for j in range(1, n+1): # 출발
        for k in range(1, n+1): # 도착
            if j != k:
                if distance[j][k] > distance[j][i] + distance[i][k]:
                    distance[j][k] = distance[j][i] + distance[i][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == INF:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()




