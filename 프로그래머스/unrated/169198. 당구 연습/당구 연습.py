def solution(m, n, startX, startY, balls):
    answer = []
    
    for targetX, targetY in balls:
        top = bottom = left = right = 0xffffff        
        if not (startX == targetX and targetY >= startY):
            top = (startX-targetX)**2 + (2*n-startY-targetY)**2        
        if not (startX == targetX and targetY <= startY):
            bottom = (startX-targetX)**2 + (-startY-targetY)**2        
        if not (startY == targetY and targetX <= startX):
            left = (-startX-targetX)**2 + (startY-targetY)**2        
        if not (startY == targetY and targetX >= startX):
            right = (2*m-startX-targetX)**2 + (startY-targetY)**2
        answer.append(min((top,bottom,left,right)))
          
    return answer

    
    