N = int(input())
nums = list(map(int, input().split()))
reverse = nums[::-1]

increase, decrease  = [1 for _ in range(N)], [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse[i] > reverse[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = 0
decrease = decrease[::-1]
for i in range(N):
    sum = increase[i] + decrease[i] - 1
    if sum > result :
        result = sum

print(result)



