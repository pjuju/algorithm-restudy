N = int(input())
crains = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))
idxs = [M] * N

if max(crains) < max(boxes):
    print(-1)
else:
    crains.sort(reverse=True)
    boxes.sort(reverse=True)

    for i in range(N):
        for j in range(M):
            if crains[i] >= boxes[j]:
                idxs[i] = j
                break
    
    visited = [0] * M
    cnt = 0
    time = 0
    while cnt < M:
        time += 1
        for i in range(N):
            for j in range(idxs[i], M):
                if not visited[j]:
                    visited[j] = 1
                    idxs[i] += 1
                    cnt += 1
                    break

    print(time)