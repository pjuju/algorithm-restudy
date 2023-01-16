import heapq
import sys
# heapq는 최소힙만 지원함. heap에 넣을 값을 음수로 만들어줘서 최대값을 출력한다.

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap)==0:
            print(0)
        else:
            min = heapq.heappop(heap)[1]
            print(min)
    else:
        heapq.heappush(heap,(-num,num)) # 우선순위, 값

