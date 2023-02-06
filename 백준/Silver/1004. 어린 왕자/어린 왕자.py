import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1,y1, x2,y2 = map(int, input().split())
    result = 0

    n = int(input())
    for _ in range(n):
        cx, cy, r = map(int, input().split())

        # 출발점과 원 중앙과의 거리
        start_dis = ((x1-cx)**2 + (y1-cy)**2) 

        # 도착점과 원 중앙과의 거리
        end_dis = ((x2-cx)**2 + (y2-cy)**2)

        r **= 2

        # 반지름이 더 크면 포함하고 있는 것임
        if r > start_dis or r > end_dis:
            result += 1
        
        if r > start_dis and r > end_dis:
            result -= 1

    print(result)


            
