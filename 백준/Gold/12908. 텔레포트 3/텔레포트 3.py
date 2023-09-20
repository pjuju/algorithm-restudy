def func(x, y, val):
    global result
    result = min(result, abs(ex-x) + abs(ey-y) + val)

    for i in range(6):
        if not visited[i]:
            visited[i] = 1
            ax, ay, bx, by = lst[i]
            func(bx, by, val+abs(ax-x)+abs(ay-y)+10)
            visited[i] = 0
    

sx, sy = map(int, input().split())
ex, ey = map(int, input().split())

lst = []
visited = [0] * 6
for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    lst.append((x1, y1, x2, y2))
    lst.append((x2, y2, x1, y1))

result = 1e10
func(sx, sy, 0)
print(result)

