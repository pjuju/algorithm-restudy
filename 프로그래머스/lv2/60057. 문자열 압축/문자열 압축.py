def solution(s):
    result = len(s)
    for x in range(1, len(s)//2+1):        
        cnt = 0
        temp = ''
        temp_check = 0
        for i in range(0,len(s)//x):            
            if s[x*i:x*(i+1)] != temp:
                temp = s[x*i:x*(i+1)]
                temp_check = 0
                cnt += x
            else:
                if not temp_check:                    
                    temp_check = 2
                    cnt += 1
                else:
                    cnt -= len(str(temp_check))
                    temp_check += 1
                    cnt += len(str(temp_check))
                
        
        cnt += len(s) % x
        if cnt < result:
            result = cnt
            
    return result
                
   