def find(x):
    start = 0
    end = N-1
    
    
    while start <= end:
        middle = (start+end)//2
        
        if lst[middle] == x:
            print('1')
            return
        
        elif lst[middle] > x:
            end = middle-1
            
        else:
            start = middle+1
        
    print('0')            


N = int(input())
lst = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))

for num in nums:
    find(num)
    


