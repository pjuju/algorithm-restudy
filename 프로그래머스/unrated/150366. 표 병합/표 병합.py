def solution(commands):
    answer = []   
    arr = [[False]*51 for _ in range(51)]
    parents = [[(i,j) for j in range(51)] for i in range(51)]
    childs = [[[] for i in range(51)] for j in range(51)]

    def find(r,c):        
        if parents[r][c] == (r,c):
            return (r,c)
        
        parents[r][c] = find(parents[r][c][0],parents[r][c][1])
        return parents[r][c]

    def update(r,c,text):
        nr,nc = find(r,c)
        arr[nr][nc] = text
        
    def update_text(text, new_text):
        for i in range(51):
            for j in range(51):
                if arr[i][j] == text:
                    arr[i][j] = new_text
                    
    def merge(r1,c1,r2,c2):      
        # if r1 == r2 and c1 == c2:
        #     return
        a,b = find(r1,c1)
        c,d = find(r2,c2)
        if a == c and b == d:
            return
        if arr[a][b]:            
            arr[c][d] = False
            parents[c][d] = (a,b)
            childs[a][b].append((c,d))
            childs[a][b] += childs[c][d]
            childs[c][d] = []
        else:            
            parents[a][b] = (c,d)
            childs[c][d].append((a,b))
            childs[c][d] += childs[a][b]
            childs[a][b] = []
        
    def unmerge(r,c):
        pr,pc = find(r,c)        
        val = arr[pr][pc]        
        arr[pr][pc] = False
        arr[r][c] = val 
        
        for cr,cc in childs[pr][pc]:
            parents[cr][cc] = (cr,cc)
        childs[pr][pc] = []
        
    def pprint(r,c):
        nonlocal answer
        pr,pc = find(r,c)
        text = arr[pr][pc] 
        if text == False:
            answer.append('EMPTY')
        else:
            answer.append(text)
    i = 1     
    for command in commands:

        command = command.split(' ')
        
        if command[0] == 'UPDATE':
            if len(command) == 4:
                a,b = map(int,command[1:3])
                update(a,b,command[3])
            else:
                update_text(command[1],command[2])
        
        elif command[0] == 'MERGE':
            a,b,c,d = map(int,command[1:])
            merge(a,b,c,d)
            
        elif command[0] == 'UNMERGE':
            a,b = map(int,command[1:])
            unmerge(a,b)
            
        else:
            a,b = map(int,command[1:])
            pprint(a,b)
        print(i)            
        i += 1
        for row in arr[1:5]:
            print(row[1:5])
        
    return answer   