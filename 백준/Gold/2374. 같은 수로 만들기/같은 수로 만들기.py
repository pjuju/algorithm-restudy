import sys
input = sys.stdin.readline
n = int(input())

result = 0
val = int(input()) # 이전까지 최대 값
max_val = val

for _ in range(n-1):
    x = int(input())
    max_val = max(x, max_val)
    
    if x > val:
        result += (x-val) 
    
    val = x

result += max_val-val

print(result)