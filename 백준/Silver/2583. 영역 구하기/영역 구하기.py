M, N, K = map(int, input().split())
arr = [[0]*(N) for _ in range(M)]

for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[y][x] = 1

result = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            count = 1
            arr[i][j] = 1
            queue = [(i, j)]
            while queue:
                x, y = queue.pop(0)
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                        arr[nx][ny] = 1
                        count += 1
                        queue.append((nx, ny))
            result.append(count)
print(len(result))
print(*sorted(result))

