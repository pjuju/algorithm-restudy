def bt(num):
    x = ''
    while num > 1:
        x = str(num%2) + x
        num //= 2
    result = str(num) + x
    
    y = len(result)
    i = 1
    while (2**i)-1 < len(result):
        i += 1
        
    result = '0' * ((2**i)-1-len(result)) + result
    return result

def func(left,right,bt_num):
    
    if left >= right:
        return bt_num[left]
    
    middle = (left+right)//2
    
    a = func(left,middle-1,bt_num)
    b = func(middle+1,right,bt_num)
    c = bt_num[middle]
    
    if a == False or b == False:
        return False
    
    if c == "0":
        if a == "0" and b == "0":
            return c
        else:
            return False
    return c
    
    
  
    
    
        
def solution(numbers):
    result = []
    
    for num in numbers:
        bt_num = bt(num)   
        # print(bt_num)
        x = func(0,len(bt_num)-1,bt_num)
        if x == False:
            result.append(0)
        else:
            result.append(1)
    return result
    