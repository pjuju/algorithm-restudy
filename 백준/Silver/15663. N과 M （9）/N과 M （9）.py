N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
results = []
lst = []
idx = []
def func():
    if len(lst) == M:
        ans = ' '.join(map(str,lst))
        if ans not in results:
            results.append(ans)
            print(ans)
        return

    for i in range(N):
        if i not in idx:
            idx.append(i)
            lst.append(nums[i])
            func()
            idx.remove(i)
            lst.pop()

func()
