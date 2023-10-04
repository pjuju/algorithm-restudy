import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())

stars = []
x_lst = []
y_lst = []

for _ in range(K):
    x,y = map(int, input().split())
    stars.append((x,y))
    x_lst.append(x)
    y_lst.append(y)

result = 0
for x in x_lst:
    for y in y_lst:
        val = 0
        for r,c in stars:
            if x <= r <= x+L and y <= c <= y+L:
                val += 1

        result = max(result, val)

print(K-result)