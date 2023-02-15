import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    start, end = map(int, input().split())
    heapq.heappush(arr, (end, start))

now = 0
cnt = 0
while arr:
    end, start = heapq.heappop(arr)
    if start >= now:
       cnt += 1
       now = end

print(cnt)  
