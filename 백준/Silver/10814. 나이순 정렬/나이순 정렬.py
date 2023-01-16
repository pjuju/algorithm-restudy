import sys

N = int(sys.stdin.readline().rstrip())

arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().split())

arr.sort(key=lambda x: int(x[0]))

for x in arr:
    print(f'{x[0]} {x[1]}')

