import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
sol = 0

# max_val = 0
# for row in arr:
#     max_val = max(max_val, max(row))

dr, dc = [0,0,-1,1], [1,-1,0,0]
def dfs(r,c,h):
    for k in range(4):
        nr, nc = r+dr[k], c+dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc] and arr[nr][nc] > h:
                visited[nr][nc] = 1
                dfs(nr,nc,h)

for x in range(max(map(max, arr))):
    visited = [[0] * N for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] > x and not visited[r][c]:
                result += 1
                visited[r][c] = 1
                dfs(r,c,x)

    sol = max(sol, result)

print(sol)





