import heapq
N = int(input())
lec = []
room = []

for _ in range(N):
    i,start,end = map(int, input().split())
    heapq.heappush(lec, (start,end))
    
start, end = heapq.heappop(lec)
heapq.heappush(room, end)

while lec:
    lec_start,lec_end = heapq.heappop(lec)
    room_end = heapq.heappop(room)
    heapq.heappush(room, lec_end)
    if lec_start < room_end:
        heapq.heappush(room, room_end)
        
print(len(room))