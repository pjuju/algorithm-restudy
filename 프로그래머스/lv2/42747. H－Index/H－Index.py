
def solution(citations):
    arr = sorted(citations)
    N = len(arr)
    print(arr)
    for i in range(N):

        if arr[i] >= N-i:
            result = N-i
            return result # 최소 인용 회수
    return 0
        
        
        
        
        
        
