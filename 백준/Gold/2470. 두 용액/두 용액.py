
# -99. -2. -1, 4, 98

M = int(input())
lst = sorted(list(map(int, input().split())))

val = 1e18
ans_left, ans_right = 0, 1e18

left = 0
right = M-1
while left < right:
    temp = lst[left] + lst[right]
    if abs(temp) < val:
        val = abs(temp)
        ans_left, ans_right = lst[left], lst[right]
    
    if temp > 0:
        right -= 1
    else:
        left += 1
        
print(ans_left, ans_right)
    
