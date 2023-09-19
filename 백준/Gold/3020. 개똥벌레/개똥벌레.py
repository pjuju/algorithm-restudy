import sys
input = sys.stdin.readline

N, H = map(int, input().split())
up_dp = [0] * (H+1)
down_dp = [0] * (H+1)
dp = [0] * (H+1)

for i in range(1, N+1):
    x = int(input())
    if i % 2 : # 홀
        down_dp[x] += 1
    else:
        up_dp[x] += 1

for h in range(H-1, -1, -1):
    down_dp[h] += down_dp[h+1]
    up_dp[h] += up_dp[h+1]

result = 1e9
cnt = 0
for h in range(1, H+1):
    dp[h] = down_dp[h] + up_dp[H-h+1]

    if dp[h] < result:
        result = dp[h]
        cnt = 1
    
    elif dp[h] == result:
        cnt += 1

print(result, cnt)
