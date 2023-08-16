N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
result = []

def func(i, temp):
    if len(temp) == M:
        if temp not in result:
            result.append(temp)
            print(*temp)
        return
    
    for j in range(i+1, N):        
        func(j, temp+[lst[j]])
        

func(-1,[])

