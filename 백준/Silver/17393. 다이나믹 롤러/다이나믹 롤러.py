N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = []
for x in range(N):
    l,r = x+1, N-1
    tmp = x
    while l <= r:        
        mid = (l+r)//2        
        if A[x] >= B[mid]:
            l = mid+1
            tmp = mid
        else:
            r = mid-1
    answer.append(tmp-x)

print(*answer)
