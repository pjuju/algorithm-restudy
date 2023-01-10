import sys
input = sys.stdin.readline

a,b = map(int, input().split())
nums = list(map(int, input().split()))

sum_list = [0]
temp = 0

for i in range(1, a+1):
    sum_list.append(sum_list[i-1] + nums[i-1])

for _ in range(b):
    x,y = map(int, input().split())
    print(sum_list[y]-sum_list[x-1])




