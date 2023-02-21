import sys
input = sys.stdin.readline

def func(x,y):
    if y == 0:
        return x
    
    return func(y, x%y)

a,b = map(int, input().split()) 
cnt = func(a,b)

print('1'*cnt)