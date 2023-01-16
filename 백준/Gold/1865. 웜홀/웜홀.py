def func():
    global result
    for i in range(1, 1+N):
        for j in range(1, 1+N):
            for to, cost in streets[j]:
                if dis[to] > cost + dis[j]:
                    dis[to] = cost + dis[j]
                    if i == N:
                        result = "YES"
    # 벨만포드 알고리즘은 노드의 갯수가 N개라고 하면, 벨만 포드 알고리즘은 N-1번의 순환 이내에 최적화된 경로를 반드시 뱉어낸다.


T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    streets = [[] for _ in range(N+1)]
    INF = 0xfffffff
    dis = [INF] * (N+1)
    # 도로
    for _ in range(M):
        S, E, T = map(int, input().split())
        streets[S].append((E, T))
        streets[E].append((S, T))

    # 웜홀
    for _ in range(W):
        S, E, T = map(int, input().split())
        streets[S].append((E, -T))

    result = "NO"
    func()

    print(result)











