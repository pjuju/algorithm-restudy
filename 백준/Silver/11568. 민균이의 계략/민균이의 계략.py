import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums = [0] + nums
dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(i-1, -1, -1):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
        
print(max(dp))
    