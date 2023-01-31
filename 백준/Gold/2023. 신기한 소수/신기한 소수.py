N = int(input())

def is_prime(x):
    for i in range(2, int(x/2)+1):
        if x % i == 0:
            return False
    return True

def dfs(n):
    if len(str(n)) == N:
        print(n)
        return
    
    for i in range(0, 5):
        i = i*2 + 1
        next = int(str(n) + str(i))
        if is_prime(next):
            dfs(next)

sosus = [2,3,5,7]      
for sosu in sosus:
    dfs(sosu)