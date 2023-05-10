from collections import deque

N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
for _ in range(K):
    r,c = map(int, input().split())
    arr[r-1][c-1] = 1

# 상0 우1 하2 좌3
dr, dc = [-1,0,1,0], [0,1,0,-1]
time, direction = 0,1

dq = deque()
dq.append((0,0))
r,c = 0,0
visited[r][c] = 1

result = 0
L = int(input())
for _ in range(L):
    X, C = input().split()

    if result:
        continue
    
    while time < int(X):
        time += 1
        r, c = r+dr[direction], c+dc[direction]
        if not (0<=r<N and 0<=c<N) or visited[r][c]:
            result = time
            break
        else:
            if not arr[r][c]:
                pr,pc = dq.popleft()
                visited[pr][pc] = 0
            arr[r][c] = 0
            visited[r][c] = 1
            dq.append((r,c))
            
            
    if C == 'L':
        direction -= 1
        if direction < 0:
            direction = 3
    else:
        direction = (direction+1) % 4

while not result:
    time += 1
    r, c = r+dr[direction], c+dc[direction]
    if not (0<=r<N and 0<=c<N) or visited[r][c]:
        result = time
        break
    else:
        if not arr[r][c]:
            pr,pc = dq.popleft()
            visited[pr][pc] = 0
        arr[r][c] = 0
        visited[r][c] = 1
        dq.append((r,c))
            

print(result)