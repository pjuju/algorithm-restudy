import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
queue = deque()

for _ in range(T):
    N, K = map(int, input().split())   
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    cnt = [0] * (N+1)  
    time_dp = [0] * (N+1)
    
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        cnt[b] += 1
        
    W = int(input())   
    
    for i in range(1, N+1):
        if cnt[i] == 0:
            queue.append(i)
            time_dp[i] = time[i]
    
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            time_dp[y] = max(time_dp[y], time[y]+time_dp[x])
            cnt[y] -= 1
            if cnt[y] == 0:
                queue.append(y)
                    
    print(time_dp[W])