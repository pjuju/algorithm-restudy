N = int(input())
nums = list(map(int,input().split()))

ans = [-1] * N
stack = []

for i in range(N):
    while stack:
        if nums[stack[-1]] < nums[i]:
            ans[stack.pop()] = nums[i]
        else:
            break
    stack.append(i)

print(*ans)