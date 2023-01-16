N, M = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
result = []
def func(x):
    if len(result) == M:
        print(*result)
        return

    for i in range(x, len(nums)):
        result.append(nums[i])
        func(i)
        result.pop()

func(0)

