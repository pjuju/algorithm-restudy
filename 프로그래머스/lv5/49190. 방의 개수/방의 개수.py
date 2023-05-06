from collections import defaultdict

def solution(arrows):
    dr, dc = [1,1,0,-1,-1,-1,0,1], [0,1,1,1,0,-1,-1,-1]
    answer = 0
    
    visit = defaultdict(list)
    r, c = 0,0
    for x in arrows:
        for _ in range(2):
            nr, nc = r+dr[x], c+dc[x]        
            # 방문한적 있을 때
            if (nr,nc) in visit:
                # 같은 방향에서 온 적 없으면
                if (r,c) not in visit[(nr,nc)]:                
                    answer += 1
                    visit[(nr,nc)].append((r,c))
                    visit[(r,c)].append((nr,nc))       
            
            else:
                visit[(nr,nc)].append((r,c))
                visit[(r,c)].append((nr,nc))    
            

            r, c = nr, nc
   
    return answer