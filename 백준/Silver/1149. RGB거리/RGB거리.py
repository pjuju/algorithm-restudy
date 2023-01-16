# def func(now_home, n, cost):
#     global result
#     if cost >= result:
#         return
#     if n == N:
#         if cost < result:
#             result = cost
#         return
#     for next_home in range(3):
#         if next_home != now_home:
#             func(next_home, n+1, cost+homes[n][next_home])

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
# result = 0xffffffffff
# func(3, 0, 0)

for i in range(1, N):
    costs[i][0] += min(costs[i-1][1], costs[i-1][2])
    costs[i][1] += min(costs[i-1][0], costs[i-1][2])
    costs[i][2] += min(costs[i-1][0], costs[i-1][1])

print(min(costs[N-1]))
