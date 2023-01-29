import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
result = [-1] * N

stack = []

for i in range(N):
    while stack:
        if nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        else:
            break
    stack.append(i)
    
print(*result)
    