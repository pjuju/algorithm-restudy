import heapq

N, K = map(int, input().split())
hq = []
heapq.heappush(hq, (0,N))

visited = set()

while hq:
    time, now = heapq.heappop(hq)
    if now == K:
        print(time)
        break

    if now in visited:
        continue
    
    visited.add(now)

    if now*2 <= 100000:
        if now*2 not in visited:
            heapq.heappush(hq, (time, now*2))


    for next in (now+1, now-1):
        if 0 <= next <= 100000:
            if next not in visited:
                heapq.heappush(hq, (time+1, next))
    
