N = int(input())
M = int(input())
fix = [int(input()) for _ in range(M)]

dp = [0] * (40+1)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, 40+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
pre = 0

if fix:    
    for f in fix:
        answer *= dp[f-1-pre]
        pre = f
    answer *= dp[N-pre]     
else:
    answer = dp[N]

print(answer)