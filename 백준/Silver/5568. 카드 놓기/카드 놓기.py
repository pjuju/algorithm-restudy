n = int(input())
k = int(input())
cards = [input() for _ in range(n)]

visited = [0] * n
result = set()
def perm(x,word):
    
    if x == k:
        result.add(word)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            perm(x+1,word+cards[i])
            visited[i] = 0
              
perm(0,'')
print(len(result))