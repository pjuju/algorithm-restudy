N = int(input())
nums = list(map(int, input().split()))
if N == 1:
    print(nums[0])

else:
    for i in range(1, N):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]

    print(max(nums))
