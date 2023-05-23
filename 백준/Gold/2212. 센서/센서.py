import sys
input = sys.stdin.readline
import heapq

N = int(input())
K = int(input())
position = sorted(list(map(int, input().split())))
distance = []

for i in range(N-1):
    heapq.heappush(distance, -position[i+1] + position[i])

for _ in range(K-1):
    if distance:
        heapq.heappop(distance)

print(-sum(distance))