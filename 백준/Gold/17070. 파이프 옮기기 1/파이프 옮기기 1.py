N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * (N) for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1
# print(dp)

for r in range(N):
    for c in range(N):

        # 0 (가로)
        if dp[0][r][c]:
            ## 1) 가로(0) / (r,c+1)   
            if r < N and c+1 < N and not arr[r][c+1]:
                dp[0][r][c+1] += dp[0][r][c]
            ## 2) 대각선(2) / (r+1,c+1) 
            if r+1 < N and c+1 < N:
                if not arr[r+1][c] and not arr[r][c+1] and not arr[r+1][c+1]:
                    dp[2][r+1][c+1] += dp[0][r][c] 

        # 1 (세로)
        if dp[1][r][c]:
            ## 1) 세로(1) / (r+1, c)
            if r+1 < N and c < N and not arr[r+1][c]:
                dp[1][r+1][c] += dp[1][r][c]
            ## 2) 대각선(2) / (r+1, c+1)
            if r+1 < N and c+1 < N:
                if not arr[r+1][c] and not arr[r][c+1] and not arr[r+1][c+1]:
                    dp[2][r+1][c+1] += dp[1][r][c] 

        # 2 (대각선)
        if dp[2][r][c]:
            ## 1) 가로(0) / (r,c+1)   
            if r < N and c+1 < N and not arr[r][c+1]:
                dp[0][r][c+1] += dp[2][r][c]
            ## 2) 세로(1) / (r+1, c)
            if r+1 < N and c < N and not arr[r+1][c]:
                dp[1][r+1][c] += dp[2][r][c]
            ## 3) 대각선(2) / (r,c+1) 
            if r+1 < N and c+1 < N:
                if not arr[r+1][c] and not arr[r][c+1] and not arr[r+1][c+1]:
                    dp[2][r+1][c+1] += dp[2][r][c] 
        
result = 0
for i in range(3):
    result += dp[i][N-1][N-1]            
print(result)
