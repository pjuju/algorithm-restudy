T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    
    if N == M:
        if sum(lst) < K:
            print(1)
        else:
            print(0)
            
    else:
        for i in range(M):
            lst.append(lst[i])
        
        sub_sum = [0]
        for i in range(N+M):
            sub_sum.append(sub_sum[i]+lst[i])
    
        cnt = 0
        for i in range(N):
            if sub_sum[i+M]-sub_sum[i] < K:
                cnt += 1
        
        print(cnt) 