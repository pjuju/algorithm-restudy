import sys
input = sys.stdin.readline

N, attack = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

left = 1
right = int(1e18)
answer = 0

while left <= right:
    mid = (left+right)//2
    hp = mid
    att = attack
    for a,b,c in lst:
        if a == 1:
            cnt = c // att
            if not c%att:
                cnt -= 1
            hp -= (b*cnt)
            if hp <= 0:                
                break
        else:
            hp = min(mid, hp+c)
            att += b
    if hp > 0 :
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
        
print(answer)