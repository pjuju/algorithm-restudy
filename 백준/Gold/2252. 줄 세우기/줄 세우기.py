import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
cnt = [0] * (N+1)
for _ in range(M):
    A,B = map(int, input().split())
    graph[A].append(B)
    cnt[B] += 1

result = []
while len(result) < N:
    for i in range(1, len(cnt)):
        if cnt[i] == 0:
            cnt[i] -= 1
            result.append(i)
            for x in graph[i]:
                cnt[x] -= 1
            

print(*result)