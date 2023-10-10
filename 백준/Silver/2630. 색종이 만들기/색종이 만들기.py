# 1. 각 왼쪽위 지점 4개가 붙어있고 색이 같을 때 합칠 수 있음
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
check = [[1] * N for _ in range(N)]

blue = white = 0
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            blue += 1
        else:
            white += 1

x = 1
l = 0
while x != N:
    x *= 2
    l += 1

for a in range(1, l+1):
    for r in range(0, N, 2**a):
        for c in range(0, N, 2**a):
            for nr, nc in ((r+2**(a-1), c), (r,c+2**(a-1)), (r+2**(a-1), c+2**(a-1))):
                if not check[nr][nc] or arr[r][c] != arr[nr][nc]:
                    check[r][c] = 0
                    break
            if check[r][c]:
                if arr[r][c]:
                    blue -= 3
                else:
                    white -= 3
                    
print(white)
print(blue)


            






