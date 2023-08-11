import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
position = list(map(int, input().split()))
position.sort()

def search(x):
    start, end = 0, M-1
    
    while start <= end:
        mid = (start+end)//2
        
        if position[mid] >= x:
            end = mid-1
        else:
            start = mid+1
            
    return end 

cnt = 0
for _ in range(N):
    a,b = map(int, input().split())
    if b > L:
        continue
    idx = search(a)
    for i in (idx-1, idx, idx+1):
        if 0<=i<M:            
            if abs(position[i]-a) + b <= L:
                cnt += 1
                break
    
print(cnt)   
    # position에서 a랑 가장 가까운 값
    