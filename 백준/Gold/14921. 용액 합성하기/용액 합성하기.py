N = int(input())
lst = list(map(int, input().split()))
left = 0
right = N-1
result = 1e9
while right>left:
    val = lst[left] + lst[right]
    if val == 0:
        result = 0
        break
    if abs(lst[left]+lst[right]) < abs(result):
        result = lst[left]+lst[right]
    elif val > 0:
        right -= 1
    else:
        left += 1
print(result)