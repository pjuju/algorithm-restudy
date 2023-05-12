import sys
input = sys.stdin.readline

N, K = map(int, input().split())
words = [list(input())[4:-4] for _ in range(N)]

K -= 5
learned = [0] * 26
for t in 'antic':
    learned[ord(t)-ord('a')] = 1
    
def learn(i, cnt):
    global result
    
    if cnt == K:
        can_read = 0
        for word in words:
            flag = True
            for s in word:
                if not learned[ord(s)-ord('a')]:
                    flag = False
                    break
            if flag:
                can_read += 1
                
        if can_read > result:
            result = can_read                
        return
    
    for j in range(i+1, 26):
        if not learned[j]:
            learned[j] = 1
            learn(j, cnt+1)
            learned[j] = 0

result = 0
if K > 0:  
    for x in range(26):
        if not learned[x]:
            learned[x] = 1
            learn(x, 1)
            learned[x] = 0
            
elif K == 0:
    can_read = 0
    for word in words:
        flag = True
        for s in word:
            if not learned[ord(s)-ord('a')]:
                flag = False
                break
        if flag:
            can_read += 1
            
    if can_read > result:
        result = can_read          
   
print(result)