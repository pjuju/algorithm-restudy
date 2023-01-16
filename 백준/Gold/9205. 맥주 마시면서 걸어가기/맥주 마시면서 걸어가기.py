tc = int(input())
for t in range(tc):
    n = int(input())
    home = list(map(int, input().split()))
    conv = [list(map(int, input().split())) for _ in range(n)]
    fest = list(map(int, input().split()))
    conv.append(fest)
    result = 'sad'
    queue = [home]
    


    while queue:

        now = queue.pop(0)
        x1, y1 = now[0], now[1]

        if now == fest:
            result = 'happy'
            break

        for to in conv:

            x2, y2 = to[0], to[1]
            distance = abs(x1-x2) + abs(y1-y2)
            if distance <= 1000:

                queue.append(to)
                conv.remove(to)


    print(result)

