import sys
read = sys.stdin.readline

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def func(i,j):
    visited[i][j] = 1
    global nums
    nums += 1
    for x in range(4):
        nr = i + dr[x]
        nc = j + dc[x]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] and not visited[nr][nc]:
                func(nr,nc)



N = int(read())
arr = [list(map(int,read().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
nums = 0
nums_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] and not visited[i][j]:
            func(i,j)
            nums_list.append(nums)
            nums = 0
nums_list.sort()
print(len(nums_list))
for num in nums_list:
    print(num)
