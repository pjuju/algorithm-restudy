target = input()
text = [input() for _ in range(2)]
dp = [[[0] * len(text[0]) for _ in range(len(target))] for _ in range(2)]

for x in range(2):
    cnt = 0
    for i in range(len(text[0])):
        if target[0] == text[x][i]:
            cnt += 1
        dp[x][0][i] = cnt

for i in range(1, len(target)):
    for case in range(2):
        for j in range(1, len(text[0])):
            dp[case][i][j] = dp[case][i][j-1]
            if target[i] == text[case][j]:                
                dp[case][i][j] += dp[(case+1)%2][i-1][j-1]

result = dp[0][-1][-1] + dp[1][-1][-1]    
print(result)