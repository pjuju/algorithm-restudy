import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]
result = 0

start, end = 1, max(lst) * M
while start <= end:
    mid = (start+end)//2
    
    cnt = 0
    for x in lst:
        cnt += mid//x
    
    if cnt >= M:
        result = mid
        end = mid-1
    
    else:
        start = mid+1
        
print(int(result))

