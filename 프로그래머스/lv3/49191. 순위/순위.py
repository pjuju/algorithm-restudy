from collections import deque 

def solution(n, results):
    win_graph = [[] for _ in range(n+1)]
    lose_graph = [[] for _ in range(n+1)]
    for a, b in results:
        win_graph[a].append(b)
        lose_graph[b].append(a)
    
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        dq = deque()
        visited = [0] * (n+1)
        
        for win in win_graph[i]:
            visited[win] = 1
            dq.append(win)
            
        while dq:
            win = dq.popleft()
            cnt += 1
            for can_win in win_graph[win]:
                if not visited[can_win]:
                    visited[can_win] = 1
                    dq.append(can_win)
        
        dq = deque()
        for lose in lose_graph[i]:
            visited[lose] = 1
            dq.append(lose)
            
        while dq:
            lose = dq.popleft()
            cnt += 1
            for can_lose in lose_graph[lose]:
                if not visited[can_lose]:
                    visited[can_lose] = 1
                    dq.append(can_lose)
        
        if cnt == n-1:
            answer += 1

    return answer