import sys
input = sys.stdin.readline

N, M = map(int ,input().split())
nums = list(map(int, input().split()))

# 구간합 배열
part_sum = [0] * N

# 구간합 세팅
part_sum[0] = nums[0]
for i in range(1, N):
    part_sum[i] = part_sum[i-1] + nums[i]
    
# 나머지 개수 배열
remainders = [0] * M

# 각 구간합 별 3으로 나눈 나머지
for i in range(N):
    remainder = part_sum[i] % M
    remainders[remainder] += 1
    
# 그 자체로 0인 경우의 수 더하기
result = 0
result += remainders[0]

# 경우의 수 구해서 더하기
for i in range(M):
    result += remainders[i] * (remainders[i]-1) // 2
    
print(result)