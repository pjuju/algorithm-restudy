from collections import deque

N, L = map(int, input().split())
nums = list(map(int, input().split()))
queue = deque()
result = []

for i in range(N):
    while queue and nums[i] < queue[-1][1]:
        queue.pop()
    queue.append((i, nums[i]))
    
    if queue[0][0] < i-L+1:
        queue.popleft()
        
    result.append(queue[0][1])

print(*result)
