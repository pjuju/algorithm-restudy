import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    ranking = [0] * (N+1)
    a_rank = [0] * (N+1)
    b_rank = [0] * (N+1)
    for i in range(1, N+1):
        a,b = map(int, input().split())
        ranking[i] = (a,b)
        a_rank[a] = i
        b_rank[b] = i
    
    result = N
    for i in range(1, N+1):
        a, b = ranking[i]
        # print(set(a_rank[1:a] + b_rank[1:b]), a+b-2)
        if len(set(a_rank[1:a] + b_rank[1:b])) != a+b-2:
            result -= 1

    print(result)
        

