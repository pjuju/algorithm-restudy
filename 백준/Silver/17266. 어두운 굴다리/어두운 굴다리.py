import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

lst = list(map(int, input().split()))

def check(d):        
    tmp = 0
    for x in lst:
        if x-d <= tmp:
            tmp = x+d        
        else:
            return False
    if tmp >= N:
        return True
    else:
        return False

s, e, answer = 0, N, N
while s <= e:
    m = (s+e)//2
    if check(m):
        answer = m
        e = m-1
    else:
        s = m+1

print(answer)


