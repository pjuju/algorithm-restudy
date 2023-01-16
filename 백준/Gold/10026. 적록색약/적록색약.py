import sys
sys.setrecursionlimit(10**5)

dr, dc = [1,-1,0,0], [0,0,1,-1]

def rgb(i,j):
    rgb_visited[i][j] = 1
    for x in range(4):
        ni,nj = i+dr[x], j+dc[x]
        if 0<=ni<N and 0<=nj<N and not rgb_visited[ni][nj]:
            if arr[ni][nj] == arr[i][j]:
                rgb(ni,nj)


def jrsy(i,j):
    jrsy_visited[i][j] = 1
    for x in range(4):
        ni, nj = i + dr[x], j + dc[x]
        if 0 <= ni < N and 0 <= nj < N and not jrsy_visited[ni][nj]:
            if not (arr[ni][nj]+arr[i][j])%2:
                jrsy(ni, nj)

N = int(input())
arr = [list(input()) for _ in range(N)]
rgb_visited = [[0]*N for _ in range(N)]
jrsy_visited = [[0]*N for _ in range(N)]
rgb_cnt = 0
jrsy_cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 0
        elif arr[i][j] == 'G':
            arr[i][j] = 2
        elif arr[i][j] == 'B':
            arr[i][j] = 1


for i in range(N):
    for j in range(N):
        if not rgb_visited[i][j]:
            rgb_cnt += 1
            rgb(i,j)
        if not jrsy_visited[i][j]:
            jrsy_cnt += 1
            jrsy(i,j)


print(f'{rgb_cnt} {jrsy_cnt}')