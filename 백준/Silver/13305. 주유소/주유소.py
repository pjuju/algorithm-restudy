N = int(input())
distacne = list(map(int, input().split()))
prices = list(map(int, input().split()))
price = prices[0]
result = i = 0
while i < N-1:
    if prices[i] < price:
        price = prices[i]
    result += distacne[i] * price
    i += 1
print(result)

