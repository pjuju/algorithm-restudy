N, M = map(int, input().split())

def func(nums):
    if len(nums) == M:
        print(*nums)
        return

    for num in range(1, N+1):
        if num >= nums[-1]:
            new_nums = nums + [num]
            func(new_nums)


for i in range(1, N+1):
    func([i])
