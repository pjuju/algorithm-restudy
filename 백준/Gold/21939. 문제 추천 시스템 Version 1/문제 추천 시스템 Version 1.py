import sys
input = sys.stdin.readline
from collections import defaultdict 
import heapq

N = int(input())

levels = defaultdict(int)
hq = []
r_hq = []

for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(hq, (L, P))
    heapq.heappush(r_hq, (-L, -P))
    levels[P] = L

M = int(input())
for _ in range(M):
    command = input().split()
    if command[0] == 'recommend':
        if command[1] == '1':
            # print(r_hq)
            while True:
                level, pro = heapq.heappop(r_hq)
                level, pro = -level, -pro
                if levels[pro] == level:
                    print(pro)    
                    break  
            heapq.heappush(r_hq, (-level, -pro))
        else:
            while True:
                level, pro = heapq.heappop(hq)
                if levels[pro] == level:
                    print(pro)    
                    break     
            heapq.heappush(hq, (level, pro))   
                
    elif command[0] == 'add':
        level, pro = int(command[2]), int(command[1])
        heapq.heappush(hq, (level, pro))
        heapq.heappush(r_hq, (-level, -pro))
        levels[pro] = level
     
    elif command[0] == 'solved':
        pro = int(command[1])
        levels[pro] = -1
    
            