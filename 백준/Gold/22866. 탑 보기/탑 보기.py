N = int(input())
lst = list(map(int, input().split()))
from collections import deque

# 높은 것만 볼 수 있음
# 보다 높은게 있으면 더 이상 못봄
cnts = [0] * N
vals = [2*N] * N


queue = []
for i in range(N):

    while queue and queue[-1][0] <= lst[i]:
        queue.pop()

    cnts[i] += len(queue)
    if queue:
        vals[i] = queue[-1][1]


    queue.append((lst[i], i))


queue = []
for i in range(N-1, -1, -1):

    while queue and queue[-1][0] <= lst[i]:
        queue.pop()

    cnts[i] += len(queue)

    if queue:
        if abs(vals[i]-i) > queue[-1][1]-i:
            vals[i] = queue[-1][1]

    queue.append((lst[i], i))

for i in range(N):
    if cnts[i]:
        print(cnts[i], vals[i]+1)
    else:
        print(0)