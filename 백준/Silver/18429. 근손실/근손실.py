N, K = map(int, input().split())
gains = list(map(int, input().split()))
gains.sort(reverse = True)
result = 0
visited = [0] * (N)
def func(val, day):
    global result
    
    if day == N:
        result += 1
        return
    
    for i in range(N):
        if not visited[i] and val + gains[i] >= (day+1)*K:
            visited[i] = 1
            func(val + gains[i], day+1)
            visited[i] = 0

func(0,0)
print(result)