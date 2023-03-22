from collections import deque

def solution(board):
    R = len(board)    
    C = len(board[0])
    
    visited = [[-1] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'G':
                goal = (i,j)
            elif board[i][j] == 'R':
                start = (i,j)
    visited[start[0]][start[1]] = 0
    queue = deque([start])
    
    dr,dc = [0,0,1,-1],[1,-1,0,0]
    while queue:
        r,c = queue.popleft()
        if (r,c) == goal:
            return visited[r][c]
        
        # 왼쪽
        left_c = c
        while left_c != 0:
            left_c -= 1
            if board[r][left_c] == 'D':
                left_c += 1
                break
        
        # 오른쪽
        right_c = c       
        while right_c != C-1:
            right_c += 1
            if board[r][right_c] == 'D':
                right_c -= 1
                break
        
        # 아래쪽
        bottom_r = r
        while bottom_r != 0:
            bottom_r -= 1
            if board[bottom_r][c] == 'D':
                bottom_r += 1
                break
        
        # 위쪽
        top_r = r
        while top_r != R-1:
            top_r += 1
            if board[top_r][c] == 'D':
                top_r -= 1
                break   
        for nr,nc in ((top_r,c),(bottom_r,c),(r,left_c),(r,right_c)):
            if visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr,nc))
                    
    return -1