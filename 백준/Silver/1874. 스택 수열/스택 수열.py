import sys
input = sys.stdin.readline

n = int(input())
now = 0
results = []
queue = []
flag = True

for _ in range(n):
    num = int(input())
    if now < num:
        while now < num:         
            now += 1
            results.append('+')
            queue.append(now)
    
    x = queue.pop()
    if x == num:
        results.append('-')
    
    else:
        print('NO')
        flag = False
        break   
  
if flag:
    for result in results:
        print(result)
        
        


