# 가장 큰 수가 그 뒤의 수들을 더한 값 보다 작아야함
N = int(input())
lst = list(map(int, input().split()))
lst.sort()


if N > 2:    
    result = 2
    for left in range(N-2):
        right = left+2
        cnt = 2
        while True:
            if right < N and lst[left] + lst[left+1] > lst[right]:
                cnt += 1
                right += 1
            else:
                if cnt > result :
                    result = cnt
                break
else:
    result = N 
            
print(result)