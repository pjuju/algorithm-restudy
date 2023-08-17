N = int(input())
road = list(input())

dp = [1e8]*(N)
dp[0] = 0

B_lst = []
O_lst = []
J_lst = []

for i in range(N):
    if road[i] == 'B':
        B_lst.append(i)
    elif road[i] == 'O':
        O_lst.append(i)
    else:
        J_lst.append(i)

for i in range(N):
    if road[i] == 'B':
        for j in J_lst:
            if j > i:
                break
            dp[i] = min(dp[i], dp[j]+(i-j)**2)   
    elif road[i] == 'O':
        for j in B_lst:
            if j > i:
                break
            dp[i] = min(dp[i], dp[j]+(i-j)**2)  
    elif road[i] == 'J':
        for j in O_lst:
            if j > i:
                break
            dp[i] = min(dp[i], dp[j]+(i-j)**2)  

print(dp[-1] if dp[-1] != 1e8 else -1)