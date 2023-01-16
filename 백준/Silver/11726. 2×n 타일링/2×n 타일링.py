N = int(input())
dp = [0]*(N+1)
def func(n):
    if n <= 3:
        return n

    if dp[n]:
        return dp[n]

    dp[n] = func(n-1) + func(n-2)
    return dp[n]

print(func(N)%10007)