import sys
input = sys.stdin.readline

N,M = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)


while start<=end:
    middle = (start+end)//2
    
    val = 0
    cnt = 0
    for x in arr:
        val += x
        if val > middle:
            cnt += 1
            val = x
        
    if val > 0 :
        cnt += 1
    
    if cnt > M:
        start = middle + 1
    
    elif cnt <= M:
        end = middle-1
        

print(start)