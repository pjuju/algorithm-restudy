from collections import deque



def solution(n, m, x, y, r, c, k):
    have_to_move = [0] * 4 # 하, 좌, 우 상 
    answer = ''
    t = ['d','l','r','u']
    td = r-x
    lr = c-y
    
    if td > 0:
        have_to_move[0] += td
    else:
        have_to_move[3] -= td
    if lr > 0:
        have_to_move[2] += lr
    else:
        have_to_move[1] -= lr
    
    while sum(have_to_move) < k:
        # print(answer,k,have_to_move,x,y)
        
        # 아래로 갈 수 있다면
        k -= 1
        if x < n:
            x += 1            
            answer += t[0]
            if have_to_move[0]:
                have_to_move[0] -= 1
            else:
                have_to_move[3] += 1
        elif y > 1:
            y -= 1
            answer += t[1]
            if have_to_move[1]:
                have_to_move[1] -= 1
            else:
                have_to_move[2] += 1
                
        elif y < m:
            y += 1
            answer += t[2]
            if have_to_move[2]:
                have_to_move[2] -= 1
            else:
                have_to_move[1] += 1
        
    print(answer, k, have_to_move)
    
    if sum(have_to_move) != k:
        return 'impossible'

        
    for x in range(4):
        answer += (t[x] * have_to_move[x])
    return answer



