from collections import deque



def solution(x, y, n):
    
    queue = deque()
    queue.append((x,0))
    visited = [0] * (y+1)
    while queue:
        a,cnt = queue.popleft()
        if a == y:
            return cnt
        for b in (a+n, a*2, a*3):
            if b <= y:
                if not visited[b]:
                    queue.append((b,cnt+1))
                    visited[b] = 1
    return -1