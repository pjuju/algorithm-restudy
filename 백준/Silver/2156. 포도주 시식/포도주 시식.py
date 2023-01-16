N = int(input())
drink = [int(input()) for _ in range(N)]
dp = [0] * (N+1)

dp[0] = drink[0]
if N >= 2:
    dp[1] = drink[0]+drink[1]
if N >= 3:
    dp[2] = max(drink[2]+drink[1], drink[2]+drink[0], dp[1])

for i in range(3,N):
                # 전dp,    전전dp+지금,       전전전dp+전+지금
    dp[i] = max(dp[i-1], dp[i-2]+drink[i], dp[i-3]+drink[i-1]+drink[i])

# func(0,0,0)
print(dp[N-1])

