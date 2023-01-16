# text_a = input()
# text_b = input()
# # result = 0
# # def func(i,j,n):
# #     global result
# #     if n > result:
# #         result = n
# #
# #     for i in range(i, len(text_a)):
# #         for j in range(j, len(text_b)):
# #             if text_a[i] == text_b[j]:
# #                 func(i+1,j+1,n+1)
# #                 break
# #
# # func(0,0,0)
# print(result)


text_a = ' ' + input()
text_b = ' ' + input()

dp = [[0]*(len(text_b)) for _ in range(len(text_a))]
for r in range(1, len(text_a)):
    for c in range(1, len(text_b)):
        if text_a[r] == text_b[c]:
            dp[r][c] = dp[r-1][c-1]+1

        else:
            dp[r][c] = max(dp[r-1][c], dp[r][c-1])

print(dp[-1][-1])