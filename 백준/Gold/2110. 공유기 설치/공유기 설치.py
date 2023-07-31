import sys
input = sys.stdin.readline

N,C = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()

left = 1
right = lst[-1] - lst[0]

while left <= right:
    mid = (left+right)//2
    cnt = 1

    temp = lst[0]
    for i in range(1,N):
        if lst[i]-temp >= mid:
            cnt += 1
            temp = lst[i]

    if cnt >= C:
        left = mid+1
        answer = mid

    else:
        right = mid-1

print(answer)
