import sys
input = sys.stdin.readline

x = int(input())
m,n = map(int, input().split())
A = [int(input()) for _ in range(m)]
B = [int(input()) for _ in range(n)]

a_dp = [0] * (x+1)
b_dp = [0] * (x+1)
a_dp[0] = 1
b_dp[0] = 1
if sum(A) <= x:
    a_dp[sum(A)] = 1
if sum(B) <= x:
    b_dp[sum(B)] = 1

for i in range(m):
    val = 0
    for v in range(m-1):
        val += A[(i + v) % m]
        if val > x:
            break
        a_dp[val] += 1
        
        
for i in range(n):
    val = 0
    for v in range(n-1):
        val += B[(i + v) % n]
        if val > x:
            break
        b_dp[val] += 1

result = 0
for y in range(x+1):
    result += a_dp[y] * b_dp[x-y]

print(result)

