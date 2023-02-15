import sys
input = sys.stdin.readline

M, N = map(int, input().split())
check = [0]*(N+1)

result = []
for x in range(2,N+1):
    if not check[x]:
        if x >= M:
            result.append(x)
        for y in range(x,N+1,x):
            check[y] = 1

for ans in result:
    print(ans)