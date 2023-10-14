import sys
input = sys.stdin.readline
from collections import deque

N, d, k, c = map(int, input().split())
lst = [int(input()) for _ in range(N)]
check = [0] * (d+1)
check[c] = 1

result = 0
# k개 연속으로 먹으면 c번은 무료로 줌
cnt = 1
for i in range(k-1):
    if not check[lst[i]]:
        cnt += 1
    check[lst[i]] += 1

# 초밥의 가짓수가 주어짐
for i in range(N):
    pre, next = lst[i], lst[(i+k-1)%(N)]
    if not check[next]:
        cnt += 1
    check[next] += 1
    result = max(result, cnt)

    check[pre] -= 1
    if not check[pre]:
        cnt -= 1

print(result)

    

