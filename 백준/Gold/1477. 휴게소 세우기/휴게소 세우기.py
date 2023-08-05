import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
lst = sorted(list(map(int, input().split()))) + [L]

s, e = 1, lst[-1]
while s <= e:
    mid = (s+e) // 2

    now = 0
    cnt = 0

    for next in lst:
        cnt += (next-now)//mid
        if not (next-now)%mid:
            cnt -= 1
        
        now = next
        
    if cnt <= M:
        answer = mid
        e = mid-1

    else:
        s = mid+1
        
print(answer)


            


       