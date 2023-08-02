N, M = map(int, input().split())
nums = list(map(int, input().split()))

lst = []
def func(i,val,cnt):
    if cnt == M:
        lst.append(val)
    
    for j in range(i+1, N):
        func(j, val+nums[j], cnt+1)

func(-1,0,0)
lst = sorted(list(set(lst)))

prime_list = [0] * (max(lst)+1)
for i in range(2, int(max(lst)**0.5)+1):
    for j in range(2, max(lst)//i+1):
        prime_list[i*j] = 1

answer = []
for x in lst:
    if not prime_list[x]:
        answer.append(x)

if answer:
    print(*answer)
else:
    print(-1)

