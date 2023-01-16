A, B = map(int, input().split())
#
# dp = [0xfff] * (B+1)
# dp[A] = 1
#
# def func(n):
#     if n*2 <= B and dp[n*2] > dp[n]+1:
#         dp[n*2] = dp[n]+1
#         func(n*2)
#
#     new_num = int(str(n)+'1')
#     if new_num <= B and dp[new_num] > dp[n]+1:
#         dp[new_num] = dp[n]+1
#         func(new_num)
#
# func(A)
# if dp[B] == 0xfff:
#     print(-1)
# else:
#     print(dp[B])

count = 1
while True:
    if A == B:
        break
    elif A > B or (B % 10 != 1 and B % 2 != 0):
        count = -1
        break
    elif B % 10 == 1:
        B //= 10
        count += 1
    elif B % 2 == 0:
        B //= 2
        count += 1

print(count)