
def solution(picks, minerals):
    
    def dfs(dia,iron,stone,idx,val):
        nonlocal answer
        if dia+iron+stone == 0 or idx >= len(minerals):
            if val < answer:
                answer = val
            return
        
        if dia:
            dia_val = val
            for i in range(idx, idx+5):
                if i < len(minerals):
                    dia_val += 1
            dfs(dia-1,iron,stone,idx+5,dia_val)   

        if iron:
            iron_val = val
            for i in range(idx, idx+5):
                if i < len(minerals):
                    if minerals[i] == 'diamond':
                        iron_val += 5
                    else:    
                        iron_val += 1
            dfs(dia,iron-1,stone,idx+5,iron_val)    
        if stone:
            stone_val = val
            for i in range(idx, idx+5):
                if i < len(minerals):
                    if minerals[i] == 'diamond':
                        stone_val += 25
                    elif minerals[i] == 'iron':
                        stone_val += 5
                    else:    
                        stone_val += 1
            dfs(dia,iron,stone-1,idx+5,stone_val)
                
                
    dia, iron, stone = picks[0],picks[1],picks[2]
    answer = 0xfffffff
    dfs(dia,iron,stone,0,0)
    
    return answer