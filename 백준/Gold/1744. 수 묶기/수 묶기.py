import heapq

N = int(input())
plus = []
minus = []
zero = 0
result = 0

for _ in range(N):
    num = int(input())
    if num > 1:
        heapq.heappush(plus, -num)
    elif num == 1:
        result += 1
    elif num < 0:
        heapq.heappush(minus, num)
    else:  
        zero += 1

while len(plus) >= 2:    
    a = heapq.heappop(plus)
    b = heapq.heappop(plus)   
    result += a*b

while len(minus) >= 2:
    result += heapq.heappop(minus) * heapq.heappop(minus)

if minus and not zero:
    result += minus[0]

if plus:
    result -= plus[0]
    
print(result)
