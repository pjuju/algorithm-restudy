import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
result = 0

for r in range(N-1, -1, -1):
    for c in range(M-1, -1, -1):
        if arr[r][c]:
            result += 1
            for nr in range(r+1):
                for nc in range(c+1):
                    arr[nr][nc] = (arr[nr][nc] + 1) % 2

print(result)
