N = int(input())
lst = list(map(int, input().split()))
lst.sort()
result = t = 0

for i in range(N):
    result += (t+lst[i])
    t += lst[i]

print(result)
