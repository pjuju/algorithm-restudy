nums = list(map(int, input().split()))

val = 0
for n in nums:
    val += n**2

print(val%10)