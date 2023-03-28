import sys
sys.setrecursionlimit(10**5)
def solution(maps):
    answer = []
    dr, dc = [0,0,-1,1], [1,-1,0,0]
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    def dfs(r,c):
        visited[r][c] = 1
        cnt = int(maps[r][c])
        for x in range(4):
            nr, nc = r+dr[x], c+dc[x]
            if 0<=nr<n and 0<=nc<m:
                if maps[nr][nc] != 'X' and not visited[nr][nc]:
                    cnt += dfs(nr,nc)
        return cnt
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X':
                if not visited[i][j]:
                    answer.append(dfs(i,j))
    if not answer:
        answer.append(-1)
    return sorted(answer)