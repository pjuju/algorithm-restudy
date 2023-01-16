from collections import deque

N = int(input())
queue = deque()
queue.append((N,0))
used = [0]*(10**6+1)

while queue:
    n, cnt = queue.popleft()
    if n == 1:
        print(cnt)
        break

    if n%3==0 and not used[n//3]:
        queue.append((n//3,cnt+1))
        used[n//3]=1

    if n%2==0 and not used[n//2]:
        queue.append((n//2,cnt+1))
        used[n//2]=1

    if not used[n-1]:
        queue.append((n-1, cnt + 1))
        used[n-1]=1
