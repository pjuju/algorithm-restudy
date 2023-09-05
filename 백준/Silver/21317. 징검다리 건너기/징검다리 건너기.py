import sys
input = sys.stdin.readline

N = int(input())
one_jump = [0] * (21)
two_jump = [0] * (21)

for i in range(1, N):
    a,b = map(int, input().split())
    one_jump[i] = a
    two_jump[i] = b
    
K = int(input())

dp = [[100000] * (2) for _ in range(21)]
dp[1][0] = 0
dp[2][0] = one_jump[1]
dp[3][0] = min(dp[1][0] + two_jump[1], dp[2][0] + one_jump[2])

for x in range(4, N+1):
    # 큰점프 안쓴거 -> 1개 전꺼의 0, 2개 전꺼의 0
    dp[x][0] = min(dp[x-1][0]+one_jump[x-1], dp[x-2][0]+two_jump[x-2])
    # 큰점프 쓴거 -> 1개 전꺼의 1, 2개 전꺼의 1, 3개전꺼의 0
    dp[x][1] = min(dp[x-1][1] + one_jump[x-1], dp[x-2][1] + two_jump[x-2], dp[x-3][0] + K)

print(min(dp[N]))