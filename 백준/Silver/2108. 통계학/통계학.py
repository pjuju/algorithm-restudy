n = int(input())
nums = []
for x in range(n):
    nums.append(int(input()))

# 평균
sum_v = 0
for num in nums:
    sum_v += num
mean = sum_v / len(nums)
print(round(mean))

# 중앙값
nums.sort()
middle = nums[len(nums)//2]
print(middle)

# # 최빈값 (실패)
# mean = 0,0
# for num in nums:
#     if nums.count(num) > mean:
#         mean = num

# 최빈값 (구글링)
#3 최빈값
from collections import Counter
k=Counter(nums).most_common()
if len(nums) > 1:  #만약 입력값이 하나면 , 그게 최빈값이 되므로 예외처리
    if k[0][1] == k[1][1]:print(k[1][0])
    # 최빈값의 빈도수를 비교하여, 2개이상의 최빈값이 있으면 두번째로 작은것을 출력
    else : print(k[0][0])
else : print(nums[0])

# 범위
rng = max(nums) - min(nums)
print(rng)



