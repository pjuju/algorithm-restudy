N = int(input())
M = int(input())
S = input()
P = 'I' + 'OI' * N

result = 0 

i = 0
while i <= M-2*N:
    if S[i:i+2*N+1] == P: 
        i += 2
        result += 1
        continue    
    i += 1
        
print(result)