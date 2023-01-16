N, M = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
ans = []
def func(i, n):
    if n == M:
        print(*ans)
        return

    for j in range(N):
        if nums[j] not in ans:
            ans.append(nums[j])
            func(j, n+1)
            ans.remove(nums[j])

func(-1, 0)


