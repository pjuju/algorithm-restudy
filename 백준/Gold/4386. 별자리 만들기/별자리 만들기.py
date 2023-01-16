def dis(x1,y1,x2,y2):
    return ( ((x1-x2)**2 + (y1-y2)**2)**(1/2))

N = int(input())
lst = []
for _ in range(N):
    x, y = map(float, input().split())
    lst.append([x,y])

INF = dis(1000,1000,-1000,-1000)
adj = [[INF] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        adj[i][j] = dis(lst[i][0],lst[i][1],lst[j][0],lst[j][1])

start = 0
D = adj[start]
U = [start]

result = 0
while len(U) < N:
    min_idx = -1
    min_val = INF
    for i in range(N):
        if i not in U and D[i] < min_val:
            min_idx = i
            min_val = D[i]

    U.append(min_idx)
    result += min_val

    for i in range(N):
        if D[i] > adj[min_idx][i]:
            D[i] = adj[min_idx][i]

print(round(result,2))