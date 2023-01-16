N = int(input())
nums = [int(input()) for _ in range(N)]

for i in range(N):
    for j in range(N-1-i):
        if nums[j] > nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp

for num in nums:
    print(num)