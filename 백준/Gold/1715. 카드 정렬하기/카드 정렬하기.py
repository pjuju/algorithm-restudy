import sys
input = sys.stdin.readline
from queue import PriorityQueue
N = int(input())
queue = PriorityQueue()

for _ in range(N):
    queue.put(int(input()))

ans = 0
while queue.qsize() > 1:
    card = queue.get() + queue.get()
    ans += card
    queue.put(card)

print(ans)
    



