import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap)==0:
            print(0)
        else:
            min = heapq.heappop(heap)
            print(min)
    else:
        heapq.heappush(heap,num) # 우선순위, 값

