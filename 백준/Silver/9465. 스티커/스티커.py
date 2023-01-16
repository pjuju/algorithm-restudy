T = int(input())
for tc in range(T):
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(2)]
    for c in range(1, n):
        for r in range(2):
            if c == 1:
                points[r][c] += points[(r+1)%2][c-1]
            else:
                points[r][c] = max(points[0][c-2], points[1][c-2], points[(r+1)%2][c-1]) + points[r][c]

    print(max(points[0][n-1], points[1][n-1]))
