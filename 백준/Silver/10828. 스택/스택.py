import sys
N = int(sys.stdin.readline())

stack = [0] * 1000
top = -1
for _ in range(N):
    commands = sys.stdin.readline().split()


    if commands[0] == 'push':
        top += 1
        stack[top] = commands[1]

    if commands[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1

    if commands[0] == 'size':
        print(top+1)

    if commands[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)

    if commands[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])

