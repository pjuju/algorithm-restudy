import sys
input = sys.stdin.readline

N, T = map(int, input().split())
stats = [list(map(int, input().split())) for _ in range(N)]

left = 0
right = 1e9

amount = T
for i in range(N):
    amount -= stats[i][0]
    left = max(left, stats[i][0])
    right = max(right, stats[i][1])
    
result = -1
if amount >= 0:
    while left <= right:
        mid = (left+right)//2
        
        can = 0
        for i in range(N):        
            can += min(mid, stats[i][1])-stats[i][0]    
        
        if can >= amount:
            right = mid-1
            result = mid
        else:
            left = mid+1
        
    # 어떤 사람도 S를 초과하는 술은 받지 않게 할 수 있는,
    # 최소 3이고 최대 10이면
    # S 가 5 일 때
    # 5-3 가능
    
print(int(result))

    # S이하의 술
    # 더 줄 있는 양 => S - L
    # 더 마실 수 있는 양 => 
    # 술을 준 양은 SL
    # 술을 일단 L만큼 씩 줘
    # 총량 T를 0으로 만들어야해
    # T가 0보다 작아지면 안됨
    # 더 받을 수 있는 양은 SR => R-S야
    # 최종적으로 SR < T면 안됨