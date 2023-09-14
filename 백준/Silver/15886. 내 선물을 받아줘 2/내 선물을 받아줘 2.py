N = int(input())
lst = list(input())
parents = [i for i in range(N)]

def find(x):
    if parents[x] == x:
        return x 
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    if a > b:
        a,b = b,a
    
    a = parents[a]
    b = parents[b]
    parents[b] = a


for i in range(N):
    if lst[i] == 'E':
        if i < N-1:
            union(i+1, i)
    else:
        if i > 0:
            union(i, i-1)

result = set()
for i in range(N):
    result.add(find(i))

print(len(result))