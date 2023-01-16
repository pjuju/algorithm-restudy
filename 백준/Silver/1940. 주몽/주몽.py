N = int(input())
M = int(input())

nums = list(map(int, input().split()))
nums.sort()

count = 0

left = 0
right = N-1

while left < right:
    if nums[left] + nums[right] == M:
        count += 1
        left += 1
        right -= 1
    
    elif nums[left] + nums[right] > M:
        right -= 1
    
    else:
        left += 1

print(count)
