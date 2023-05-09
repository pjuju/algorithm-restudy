import math 
N, A, B, C, D = map(int, input().split())

# A가 가성비가 더 좋도록 만들기
if B/A > D/C:
    A,B,C,D = C,D,A,B
    
# 가성비가 안좋은 C는 A개 미만으로 구매함
# A개 이상 살때는 무적권 가성비 좋은걸로 사는게 좋으니까


result = 1e18
for c in range(0,A*C,C):    
    c_cnt = c // C  
    a_cnt = math.ceil((N-c)/A)
    if a_cnt < 0:
        a_cnt = 0
    cost = c_cnt * D + a_cnt * B
    if cost < result:
        result = cost

print(result)