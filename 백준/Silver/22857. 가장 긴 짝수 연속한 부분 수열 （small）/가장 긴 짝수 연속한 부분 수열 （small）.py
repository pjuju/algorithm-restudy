import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(N):
    nums[i] = (nums[i]) % 2

result = 0
cnt = 0
remove = 0
start = 0
end = 0

while end < N:   

    if nums[end]:
        remove += 1
        if remove == K+1:
            while not nums[start]:
                start += 1
                cnt -= 1
            remove -= 1
            start += 1

    else:
        cnt += 1
        if cnt > result:
            result = cnt

   

    end += 1
print(result)





