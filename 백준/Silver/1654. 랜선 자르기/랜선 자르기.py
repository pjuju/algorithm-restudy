K, N = map(int, input().split())

# K <= N
arr = [int(input()) for _ in range(K)]
start, end = 1, sum(arr)//N

while start <= end:
    mid = (start + end) // 2   # 중간 위치
    result = 0
    for l in arr:
        result += l//mid

    if result >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)

