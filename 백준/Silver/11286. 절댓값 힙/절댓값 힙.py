import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []
result = []

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(arr, (abs(x), x))
    else:
        if arr:
            a, b = heapq.heappop(arr)
            result.append(b)
        else:
            result.append(0)

for i in result:
    print(i)