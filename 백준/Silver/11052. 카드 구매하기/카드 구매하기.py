N = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
result = 0

def func(i, cnt, price):
    global result

    if cnt == N:
        if price >= result:
            result = price
        return

    for j in range(i, N+1):
        if cnt+j <= N:
            if dp[cnt+j] < price+cards[j]:
                dp[cnt+j] = price+cards[j]
                func(j, cnt+j, price+cards[j])

func(1, 0, 0)
print(result)



# dp



