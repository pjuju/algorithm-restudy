import sys
input = sys.stdin.readline

l = ord('z') - ord('A') + 1
x = ord('A')  
arr = [[0] * l for _ in range(l)]
N = int(input())
result = 0

for _ in range(N):
    s = input()
    a, b = ord(s[0])-x, ord(s[5])-x
    
    if a != b and not arr[a][b]:
        arr[a][b] = 1
        result += 1
    
for k in range(l):
    for i in range(l):
        for j in range(l):
            if i != j:
                if not arr[i][j]:
                    if arr[i][k] and arr[k][j]:
                        arr[i][j] = 1
                        result += 1
print(result)  
for i in range(l):
    for j in range(l):
        if arr[i][j]:
            print(f'{chr(i+x)} => {chr(j+x)}')          
            
        
