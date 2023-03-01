'''
월드 나라는 모든 도로가 일방통행인 도로이고, 싸이클이 없다. 그런데 어떤 무수히 많은 사람들이 월드 나라의 지도를 그리기 위해서, 
어떤 시작 도시로부터 도착 도시까지 출발을 하여 가능한 모든 경로를 탐색한다고 한다.

이 지도를 그리는 사람들은 사이가 너무 좋아서 지도를 그리는 일을 다 마치고 도착 도시에서 모두 다 만나기로 하였다. 
그렇다고 하였을 때 이들이 만나는 시간은 출발 도시로부터 출발한 후 최소 몇 시간 후에 만날 수 있는가? 
즉, 마지막에 도착하는 사람까지 도착을 하는 시간을 의미한다.

어떤 사람은 이 시간에 만나기 위하여 1분도 쉬지 않고 달려야 한다. 이런 사람들이 지나는 도로의 수를 카운트 하여라.

출발 도시는 들어오는 도로가 0개이고, 도착 도시는 나가는 도로가 0개이다.
'''

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
times = [0] * (n+1)
cnt = [0] * (n+1)
for _ in range(m):
    a,b,time = map(int, input().split())
    graph[a].append((b,time))
    reverse_graph[b].append((a,time))
    cnt[b] += 1

start,end = map(int, input().split())

queue = deque([start])
while queue:
    now = queue.popleft()
    for next,time in graph[now]:
        cnt[next] -= 1
        if cnt[next] == 0:
            queue.append(next)
        times[next] = max(times[next], times[now]+time)

print(times[end])
queue = deque([end])

sol = 0
visited = [0] * (n+1)
while queue:
    now = queue.popleft()
    for pre,time in reverse_graph[now]:
        if time + times[pre] == times[now]:
            sol += 1
            if not visited[pre]:
                queue.append(pre)
                visited[pre] = 1

print(sol)