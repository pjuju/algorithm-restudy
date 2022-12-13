from collections import deque
N, K = map(int, input().split())
queue = deque()
queue.append([N,0])
max = 100000
visited = [0] * (max+1)

while True:
    a = queue.popleft()
    x = a[0]
    cnt = a[1]

    if x == K:
        print(cnt)
        break

    for nx in [x-1, x+1, 2*x]:
        if 0 <= nx <= max and not visited[nx]:
            visited[nx] = 1
            queue.append([nx,cnt+1])

