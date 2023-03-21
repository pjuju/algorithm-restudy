import sys
input = sys.stdin.readline
import heapq

N = int(input())
hq = []
for _ in range(N):
    s,e = map(int, input().split())
    heapq.heappush(hq, (s,e))

room = [0]
while hq:
    s,e = heapq.heappop(hq)    
    min_time = heapq.heappop(room)

    heapq.heappush(room,e)
    if s < min_time:
        heapq.heappush(room,min_time)
    
print(len(room))
