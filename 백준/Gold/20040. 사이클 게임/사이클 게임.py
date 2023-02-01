import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(n)]

def find(x):
    if x == nums[x]:
        return x
    
    nums[x] = find(nums[x])
    return nums[x]
    

result = 0
for i in range(1, m+1):
    a,b = map(int, input().split())
    a, b = find(a), find(b)
    if a == b:
        result = i
        break
    nums[a] = nums[b] = min(nums[a], nums[b])

print(result)


    