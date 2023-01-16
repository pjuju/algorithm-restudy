N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(N):
        if j != i:
            for k in range(N):
                if k != i and k !=j:
                    v = arr[i] + arr[j] + arr[k]
                    if v <= M and v > result:
                        result = v

print(result)


