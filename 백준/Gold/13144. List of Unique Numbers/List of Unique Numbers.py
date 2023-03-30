from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = 0
visited = [0] * (100001)
def func(n):
    return (1+n)*(n/2)

lst = deque()
for i in range(N):
    if not visited[arr[i]]:
        lst.append(arr[i])
        visited[arr[i]] = 1
    else:
        x = len(lst)
        result += func(x)
        cnt = 0
        while True:
            cnt += 1
            a = lst.popleft()
            if a == arr[i]:
                break            
            visited[a] = 0
        result -= func(x-cnt)
        lst.append(arr[i])
        

result += func(len(lst))
print(int(result))
