def fact(n):
    if n <= 2:
        return n
    return n * fact(n-1)


n, m = map(int, input().split())
result = fact(n) // (fact(n-m) * fact(m))
print(result)

