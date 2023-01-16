import sys
from collections import deque
read = sys.stdin.readline
T = int(read())
for tc in range(T):
    N, M = map(int, read().split())
    order = deque([i for i in range(N)])
    target = order[M]
    queue = deque(list(map(int, read().split())))
    # print(f'N : {N}')
    # print(f'M : {M}')
    # print(f'order : {order}')
    # print(f'queue : {queue}')
    count = 0
    while queue:
        max_v = max(queue)

        if queue[0] == max_v:
            count += 1
            a = order.popleft()
            if a == M:
                print(count)
                break
            else:
                queue.popleft()
        else:
            queue.append(queue.popleft())
            order.append(order.popleft())










