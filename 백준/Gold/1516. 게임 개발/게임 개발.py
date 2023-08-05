import sys
input = sys.stdin.readline
import heapq

N = int(input())
graph = [[] for _ in range(N)]
cnt = [0] * N
time = [0] * N

for i in range(N):
    lst = list(map(int, input().split()))
    time[i] = lst[0]
    cnt[i] += (len(lst)-2)
    for x in range(1, len(lst)-1):
        graph[lst[x]-1].append(i)
        
hq = []
for i in range(N):
    if cnt[i] == 0:
        heapq.heappush(hq, (time[i], i))

while hq:
    t, now = heapq.heappop(hq)
    time[now] = t
    for next in graph[now]:
        cnt[next] -= 1
        if cnt[next] == 0:
            heapq.heappush(hq, (t+time[next], next))

for x in time:
    print(x)