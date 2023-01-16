# https://www.acmicpc.net/problem/15657

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
temp = []
def func(i, m):
    if m == M:
        print(*temp)
        return

    for j in range(i, N):
        if numbers[i] <= numbers[j]:
            temp.append(numbers[j])
            func(j, m+1)
            temp.pop()

func(0,0)
