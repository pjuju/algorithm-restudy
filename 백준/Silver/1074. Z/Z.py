N,r,c = map(int, input().split())
r += 1
c += 1
result = 0

2, 4, 2
while N >= 1:
    if r <= 2 ** (N - 1) and c <= 2 ** (N - 1):
        pass

    elif r > 2**(N-1) and c > 2**(N-1):
        result += (2**(N-1) * 2**(N-1) * 3)
        r -= 2 ** (N - 1)
        c -= 2 ** (N - 1)

    elif r <= 2 ** (N - 1) and c > 2 ** (N - 1):
        result += (2 ** (N - 1) * 2 ** (N - 1))
        c -= 2 ** (N - 1)

    elif r > 2 ** (N - 1) and c <= 2 ** (N - 1):
        result += (2 ** (N - 1) * 2 ** (N - 1) * 2)
        r -= 2 ** (N - 1)

    N -= 1

print(result)