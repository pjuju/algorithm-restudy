H, W = map(int, input().split())
lst = list(map(int, input().split()))
result = 0
for r in range(1, H+1):
    left = right = 0
    for i in range(W):
        if lst[i] >= r:
            left = i
            break
    for i in range(W-1, -1, -1):
        if lst[i] >= r:
            right = i
            break
    
    for i in range(left+1, right):
        if lst[i] < r:
            result += 1

print(result)