import sys
input = sys.stdin.readline
from collections import defaultdict

N,d,k,c = map(int, input().split())
dish = [int(input()) for _ in range(N)]
eat = defaultdict(int)

for i in range(k):
    eat[dish[i]] += 1
eat[c] += 1

result = 0
left = 0
for right in range(k, N+k):
    result = max(result, len(eat))
    
    eat[dish[left]] -= 1
    if not eat[dish[left]]:
        del eat[dish[left]]
    right %= N
    eat[dish[right]] += 1
    left += 1

print(result)
    


