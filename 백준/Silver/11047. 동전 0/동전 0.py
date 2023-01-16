N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

result = 0
while K != 0:
    if K >= arr[N-1]:
        result += (K // arr[N - 1])
        K %= arr[N-1]
    N -= 1


print(result)