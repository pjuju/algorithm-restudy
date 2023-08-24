import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
train = [deque([0] * 20) for _ in range(N)] # 1번 인덱스는 첫 좌석

for _ in range(M):      
    command = list(map(int, input().split()))

    if command[0] == 1:
        i, x = command[1]-1, command[2]-1
        train[i][x] = 1

    elif command[0] == 2:
        i, x = command[1]-1, command[2]-1
        train[i][x] = 0

    elif command[0] == 3: # 뒷칸으로 당기면 pop하고 앞에 [0] 추가
        i = command[1]-1
        train[i].pop() #
        train[i].appendleft(0)

    else: # 앞으로 당기면 popleft 하고 뒤에 [0] 추가
        i = command[1]-1
        train[i].popleft() #
        train[i].append(0)

result = []
for t in train:
    if t not in result:
        result.append(t)

print(len(result))
