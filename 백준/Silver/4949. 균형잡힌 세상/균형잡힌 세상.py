import sys
# input = sys.stdin.readline
text = ''

while text != '.':
    text = input()

    if text == '.':
        break
    stack = []
    result = 'yes'
    for s in text:
        if s in '([':
            stack.append(s)
        elif s in ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 'no'
                break

        elif s in ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = 'no'
                break

    if stack:
        result = 'no'

    print(result)


