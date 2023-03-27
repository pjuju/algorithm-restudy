from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = 'z'*2500
    dq = deque([(x, y, '', 0)])
    dir2char = {(1, 0): 'd', (0, -1): 'l', (0, 1): 'r', (-1, 0):'u'}
    
    while dq:
        x, y, direction, cnt = dq.popleft()
        if direction > answer: continue
        if cnt>= k:
            if x == r and y == c:
                answer = min(answer, direction)
            continue
        for dx, dy in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if 0<nx<=n and 0<ny<=m:
                tmp_dir = direction+dir2char[(dx, dy)]
                dq.append((nx, ny, tmp_dir, cnt+1))
                break
    return answer if answer != 'z'*2500 else 'impossible'