from itertools import permutations
K, M = map(int, input().split())
lst = []
MAX = int(str(9876543210)[:K+1])    # K개의 숫자를 고를 때 나올 수 있는 가장 큰 수

# 일단 최대 범위까지 소수 리스트 만들어 놓음
check = [0] * (MAX + 1)
check[0] = check[1] = 1
prime_lst = set()   # 있는지 체크하기에는 set 자료형이 최고
for i in range(2, MAX+1):
    if check[i] == 0:
        # check[i] = 1
        prime_lst.add(i)  # 1부터 N까지 소수 리스트
        j = 2
        while i * j <= MAX:
            check[i*j] = 1
            j+=1

def func(x):
    # 조건 2
    tmp = x
    while not tmp % M:
        tmp //= M    
    
    for i in range(2, int(tmp**0.5)+1):
        if not tmp % i:
            if not check[i] and not check[tmp//i]: 
                # 조건 2
                for j in range(x//2):
                    if not check[j] and not check[x-j]:
                        # print(i, tmp//i, j, x-j)
                        return True    
            break    
    return False

def perm(x):
    global result
    if len(x) == K:
        
        if func(int(x)):
            result += 1
        return
    
    for j in range(10):
        if not visited[j]:
            visited[j] = 1
            perm(x+str(j))
            visited[j] = 0

result = 0
visited = [0] * 10
for i in range(1, 10):
    visited[i] = 1
    perm(str(i))
    visited[i] = 0

print(result)