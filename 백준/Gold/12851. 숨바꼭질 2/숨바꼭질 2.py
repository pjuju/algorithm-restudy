import heapq
N, K = map(int, input().split())
from collections import deque

dq = deque()
costs = [float('inf')] * (100001)
cnts = [0] * (100001)
costs[N] = 0
cnts[N] = 1

visit_set = set()

dq.append(N)
visit_set.add(N)

while dq:
    now = dq.popleft()

    if now == K:
        print(costs[now])
        print(cnts[now])
        break

    for next in (2*now, now+1, now-1):
        if 0<=next<=100000:
            if costs[next] >= costs[now] + 1:
                costs[next] = costs[now] + 1
                cnts[next] += cnts[now]
            if next not in visit_set:
                visit_set.add(next)
                dq.append(next)
    



