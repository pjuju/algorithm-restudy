n = int(input())
lst = list(map(int, input().split()))

result = -1000
val = 0

for i in range(n):
    val += lst[i]
    if val > result:
        result = val
    if val < 0:
        val = 0

print(result)