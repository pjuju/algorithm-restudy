N = int(input())
nums = [[0]+ list(map(int, input().split())) + [0]*(N-1-i) for i in range(N)]

for i in range(1, N):
    for j in range(1, i+2):
        nums[i][j] += max(nums[i-1][j], nums[i-1][j-1])

print(max(nums[N-1]))

