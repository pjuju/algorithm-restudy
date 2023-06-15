import sys
input = sys.stdin.readline
import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    lst = [input().strip() for _ in range(n)]
    lst.sort()

    result = 'YES'
    now = '*'
    
    for x in lst:
        
        if now == x[:len(now)]:
            result = 'NO'
            break
        now = x
    print(result)
