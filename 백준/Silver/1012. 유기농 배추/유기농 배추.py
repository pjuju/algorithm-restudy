def func(i,j):
    if arr[i][j] == 1:
        arr[i][j] = 0
    else:
        return

    for x in range(4):
        nr = i + dr[x]
        nc = j + dc[x]
        if 0 <= nr < N and 0 <= nc < M:
            func(nr,nc)


N = int(input())
for tc in range(N):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    count = 0
    dr = [0,0,-1,1]
    dc = [1,-1,0,0]

    for _ in range(K):
        x,y = map(int, input().split())
        arr[y][x] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                count += 1
                func(i,j)

    print(count)
