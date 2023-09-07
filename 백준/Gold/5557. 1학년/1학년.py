from collections import deque
N = int(input())
nums = list(map(int, input().split()))

dp = [[0] * (21) for _ in range(N-1)]
dp[0][nums[0]] = 1

for i in range(1, N-1):
    val = nums[i]
    for x in range(21):
        if dp[i-1][x]:
            if 0 <= x+val < 21:
                dp[i][x+val] += dp[i-1][x]
            if 0 <= x-val < 21:
                dp[i][x-val] += dp[i-1][x]

print(dp[N-2][nums[-1]])
