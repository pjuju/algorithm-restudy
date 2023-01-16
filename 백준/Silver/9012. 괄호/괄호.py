import sys
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    text = list(input().rstrip())
    
    stack = []
    result = 'YES'
    for s in text:
        if s == '(':
            stack.append(s)
        if s == ')':
            if stack:
                stack.pop()
            else:
                result = 'NO'
                break
    if stack:
        result='NO'

    print(result)