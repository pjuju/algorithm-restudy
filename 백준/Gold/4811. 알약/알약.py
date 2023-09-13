import sys
input = sys.stdin.readline

arr = [[0] * 31 for _ in range(31)]
for i in range(31):
    arr[0][i] = 1

for i in range(31):
    for j in range(i, 31):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]
        
while True:
    x = int(input())
    if x == 0:
        break
    print(arr[x][x])