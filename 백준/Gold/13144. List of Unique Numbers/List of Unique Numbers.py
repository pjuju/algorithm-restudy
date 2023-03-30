import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cnt, start, end = 0, 0, 0
seq = set()
while end <= n-1:
    if nums[end] not in seq:
        seq.add(nums[end])
        end += 1 
        continue
    cnt += len(seq)
    seq.remove(nums[start])
    start += 1
cnt += len(seq) * (len(seq)+ 1) // 2
print(cnt)