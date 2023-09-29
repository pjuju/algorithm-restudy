def func(text):
    cnt = 1
    check = 0 # 0 자음 / 1 모음

    if text[0] in 'aeiou':
        check = 1 #(1)
    
    for i in range(1, len(text)):
        t = text[i]

        if t == text[i-1] and t not in 'eo':
            return False

        if t in 'aeiou': # 모음(1)
            if check: # 모음(1)
                cnt += 1
                if cnt == 3:
                    return False
            else: # 자음
                check = 1
                cnt = 1
        else: # 자음 #(0)
            if not check: # 자음 (0)
                cnt += 1
                if cnt == 3:
                    return False
            else: # 모음 (1)
                check = 0
                cnt = 1
        
    if cnt == len(text) and text[0] not in 'aeiou':
        return False
    
    return True


while True:
    temp = input().rstrip()
    if temp == 'end':
        break
    result = 'acceptable'
    if not func(temp):
        result = 'not acceptable'
    
    print(f'<{temp}> is {result}.')

        
            
        