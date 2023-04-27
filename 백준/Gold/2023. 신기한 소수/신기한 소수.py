N = int(input())

def dfs(num):
    if len(str(num)) == N:
        print(num)
        return
    
    for j in range(1,10,2):
        next = int(str(num) + str(j))
        if isPrime(next):
            dfs(next)

def isPrime(x):
    for i in range(2,x//2+1):
        if x%i == 0:
            return False
    return True

sosus = [2,3,5,7]
for sosu in sosus:
    dfs(sosu)
