import sys
input = sys.stdin.readline
 
N = int(input())
arr = [[0]*58 for _ in range(58)]
cnt = 0
for _ in range(N):
    _input = input()
    if _input[0] == _input[5]:
        continue
    if not arr[ord(_input[0])-65][ord(_input[5])-65]:
        arr[ord(_input[0])-65][ord(_input[5])-65] = 1
        cnt += 1
 
for k in range(58):
    for i in range(58):
        for j in range(58):
            if i != j and not arr[i][j] and arr[i][k] and arr[k][j]:
                arr[i][j] = 1
                cnt += 1
 
print(cnt)
for i in range(58):
    for j in range(58):
        if arr[i][j]:
            print(chr(i+65) + " => " + chr(j+65))
