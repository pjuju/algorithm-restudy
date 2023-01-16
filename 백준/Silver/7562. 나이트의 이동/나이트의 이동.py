dr = [-2,-2,-1,-1,1,1,2,2]
dc = [-1,1,-2,2,-2,2,-1,1]


def bfs(sr, sc):

    v = [[0]*N for _ in range(N)]
    queue = [(sr, sc, 0)]
    v[sr][sc] = 1

    while queue:
        r,c,cnt= queue.pop(0)

        if r == fr and c == fc:
            return cnt

        for k in range(8):
            nr, nc = r + dr[k], c + dc[k]
            if 0<=nr<N and 0<=nc<N and not v[nr][nc]:
                queue.append((nr,nc,cnt+1))
                v[nr][nc] = 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    sr, sc = map(int,input().split())
    fr, fc = map(int,input().split())
    result = bfs(sr,sc)
    print(result)

