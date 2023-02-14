import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

start = 1
end = k

while start < end:
    middle = (start+end)//2
    
    cnt = 0
    for x in range(1, N+1):
        cnt += min(N,middle//x)
    
    if cnt < k:
        start = middle+1
    
    if cnt >= k:
        end = middle
        
print(start)
    
        
        
    
    