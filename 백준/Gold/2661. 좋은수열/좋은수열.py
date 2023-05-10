N = int(input())

def func(word,cnt):
    global result 
    
    if result:
        return
    
    if cnt == N+1:
        result = word       
        print(result)
        return
    
    for n in ('1','2','3'):
        temp = word+n
        flag = True
        for c in range(1, cnt//2+1):    
            if temp[cnt-c:] == temp[cnt-2*c:cnt-c]:     
                flag = False
                break
        if flag:
            func(temp, cnt+1)
            
result = ''       
func('',1)