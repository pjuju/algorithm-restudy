import sys
read = sys.stdin.readline()
N, K = map(int, read.split())

from collections import deque
queue = deque([i for i in range(1, N+1)])
answer = []
while len(answer) < N:
    for i in range(1,K+1):
        if i == K:
            answer.append(queue.popleft())
        else:
            queue.append(queue.popleft())
answer = map(str, answer)
print('<', end='')
print(', '.join(answer), end='')
print('>')
