import heapq
N, K = map(int, input().split())
from collections import deque

dq = deque()
visit = [0] * (100001)
visit[N] = 0

dq.append((N,0))

result = 0
result_cnt = 0

while dq:
    now, cnt = dq.popleft()
    if now == K:
        result = cnt
        result_cnt += 1
        continue

    for next in (2*now, now+1, now-1):
        if 0<=next<=100000:
            if not visit[next] or visit[next] == cnt+1:
                visit[next] = cnt+1
                dq.append((next, cnt+1))
    
print(result)
print(result_cnt)


