N, K = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
end = 0
length = 0
result = 0

for start in range(N):
    while cnt <= K and end < N:
        if lst[end] % 2:
            cnt += 1
        else:
            length += 1
        end += 1
        
    if cnt <= K and end == N:
        result = max(result, length)
        break
    
    if cnt == K+1:
        result = max(result, length)
        
    if lst[start] % 2:
        cnt -= 1
    else:
        length -= 1

print(result)