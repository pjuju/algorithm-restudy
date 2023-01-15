N = int(input())
nums = list(map(int, input().split()))
nums.sort()

count = 0
for i in range(N):
    a = nums[i] 
    temp_nums = nums.copy()
    temp_nums.remove(a)

    left = 0
    right = N-2
    
    while left < right:
        val = temp_nums[left] + temp_nums[right]

        if val == a:
            count += 1
            break
        
        elif val > a:
            right -= 1
        
        else:
            left += 1 
            
print(count)  