N, S = map(int, input().split())
nums = list(map(int, input().split()))
result = 0
def func(i, val):
    global result
    if val == S:
        result += 1

    for j in range(i+1, N):
        func(j, val+nums[j])

for i in range(N):
    func(i, nums[i])

print(result)

