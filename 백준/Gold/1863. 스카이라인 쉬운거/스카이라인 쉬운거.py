import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
result = 0
stack = []
for _ in range(N):
    W, V = map(int, input().split())
    while stack and V < stack[-1]:        
        result += 1
        stack.pop()

    if not stack or stack[-1] != V:
        stack.append(V)
    

for i in range(len(stack)):
    if stack[i]:
        result += 1
    
print(result)