import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque([N])

visited = ['X'] * 100001
result = [K]

while queue:
    now = queue.popleft()
    if now == K:
        while now != N:
            result.append(visited[now])
            now = visited[now]

        print(len(result)-1)        
        print(*result[::-1])        
        break

    for next in [now*2, now+1, now-1]:
        if next >= 0 and next <= 100000 and visited[next] == 'X':
            visited[next] = now
            queue.append(next)

    


            
