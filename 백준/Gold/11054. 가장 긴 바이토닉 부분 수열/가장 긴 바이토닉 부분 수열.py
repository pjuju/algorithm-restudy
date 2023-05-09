N = int(input())
nums = list(map(int, input().split()))

inc, dec = [0]*N, [0]*N

for i in range(1, N):  
    for j in range(i):
        if nums[i] > nums[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if nums[N-i-1] > nums[N-j-1]:
            dec[N-i-1] = max(dec[N-i-1], dec[N-j-1]+1)
max_val = 0
for i in range(N):
    if inc[i] + dec[i] > max_val:
        max_val = inc[i] + dec[i] 

print(max_val+1)