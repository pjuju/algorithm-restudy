import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
result = 0

def merge_sort(s,e):
    global result
    
    m = (s+e) // 2
    if s == e:
        return
    
    merge_sort(s,m)
    merge_sort(m+1,e)
    
    for i in range(s, e+1):
        tmp[i] = nums[i]
        
    idx = s   
    left = s
    right = m+1
    
    while left <= m and right <= e:
        if tmp[left] > tmp[right]:
            result += (right-idx)
            nums[idx] = tmp[right]
            idx += 1
            right += 1
        
        else:
            nums[idx] = tmp[left]
            idx += 1
            left += 1
            
    while left <= m:
        nums[idx] = tmp[left]
        idx += 1
        left += 1
    
    while right <= e:
        nums[idx] = tmp[right]
        idx += 1
        right += 1

tmp = [0] * N
merge_sort(0, N-1)
print(result)