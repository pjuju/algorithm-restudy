import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(N)]
red_r = red_c = blue_r = blue_c = hole_r = hole_c = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 'R':
            red_r, red_c = r,c
        elif arr[r][c] == 'B':
            blue_r, blue_c = r,c
        elif arr[r][c] == 'O':
            hole_r, hole_c = r,c



def func():

    dr, dc = [-1,1,0,0], [0,0,-1,1] # 상하좌우

    dq = deque()
    dq.append((red_r,red_c,blue_r,blue_c,0))

    visited = set()
    visited.add((red_r,red_c,blue_r,blue_c))

    while dq:
        r_r, r_c, b_r, b_c, cnt = dq.popleft()
        if cnt == 10:
            return 0
        
        for x in range(4):
            r_nr, r_nc, b_nr, b_nc = r_r, r_c, b_r, b_c
            while True:
                r_nr, r_nc = r_nr+dr[x], r_nc+dc[x]
                if arr[r_nr][r_nc] == 'O':
                    break
                if arr[r_nr][r_nc] == '#':
                    r_nr, r_nc = r_nr-dr[x], r_nc-dc[x]
                    break
            while True:
                b_nr, b_nc = b_nr+dr[x], b_nc+dc[x]
                if arr[b_nr][b_nc] == 'O':
                    break
                if arr[b_nr][b_nc] == '#':
                    b_nr, b_nc = b_nr-dr[x], b_nc-dc[x]
                    break
            
            if b_nr == hole_r and b_nc == hole_c:
                continue

            elif r_nr == hole_r and r_nc == hole_c:
                return 1
                

            if b_nr == r_nr and b_nc == r_nc:
                r_move, b_move = abs(r_nr-r_r)+abs(r_nc-r_c), abs(b_nr-b_r) + abs(b_nc-b_c)
                if r_move > b_move:
                    r_nr, r_nc = r_nr-dr[x], r_nc-dc[x]
                else:
                    b_nr, b_nc = b_nr-dr[x], b_nc-dc[x]
            
            if (r_nr,r_nc,b_nr,b_nc) not in visited:
                visited.add((r_nr,r_nc,b_nr,b_nc))
                dq.append((r_nr,r_nc,b_nr,b_nc,cnt+1))
                
    return 0
print(func())