import sys
input = sys.stdin.readline
n = int(input())
lst = [0]
for _ in range(n):
    lst.append(int(input()))

dp = [0] *(len(lst))

for i in range(1,len(lst)):
    max_val = 0
    for j in range(1, i):
        if lst[i] > lst[j]:
            max_val = max(dp[j], max_val)
    dp[i] = max_val+1


print(n-max(dp))