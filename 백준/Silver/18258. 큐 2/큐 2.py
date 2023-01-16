import sys
read = sys.stdin.readline
N = int(read())
rear = front = -1
queue = [0] * N
for _ in range(N):
    commands = read().split()
    if commands[0] == 'push':
        rear += 1
        queue[rear] = commands[1]

    elif commands[0] == 'pop':
        if front == rear:
            print(-1)
        else:
            front += 1
            print(queue[front])

    elif commands[0] == 'size':
        print(rear-front)

    elif commands[0] == 'empty':
        if rear-front == 0:
            print(1)
        else:
            print(0)

    elif commands[0] == 'front':
        if front == rear:
            print(-1)
        else:
            print(queue[front+1])

    elif commands[0] == 'back':
        if front == rear:
            print(-1)
        else:
            print(queue[rear])