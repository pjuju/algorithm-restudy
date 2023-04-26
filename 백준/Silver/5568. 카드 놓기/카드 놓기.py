n = int(input())
k = int(input())
cards = [input() for _ in range(n)]

visited = [0] * n
check = []
result = 0
def perm(x,word):
    global result
    if x == k:
        if word not in check:
            result += 1
            check.append(word) 
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            perm(x+1,word+cards[i])
            visited[i] = 0
              
perm(0,'')
print(result)