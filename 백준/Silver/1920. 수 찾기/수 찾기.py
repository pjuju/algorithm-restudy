import sys
input = sys.stdin.readline

def func(x):
    s, e = 0, N-1
    while s <= e:
        mid = (s+e)//2
        if nums[mid] == x:
            return 1
        elif nums[mid] > x:
            e = mid-1
        else:
            s = mid+1
    return 0



N = int(input())
nums = sorted(list(map(int, input().split())))

M = int(input())
lst = list(map(int, input().split()))
for a in lst:
    print(func(a))