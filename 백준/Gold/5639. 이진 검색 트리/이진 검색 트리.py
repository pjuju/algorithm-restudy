import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

lst = []

# 엔터 들어올 때까지 입력
while True:
    try:
        lst.append(int(input().rstrip()))
    except:
        break


def func(root,end):
    if root>end:
        return
    
    next_right = end+1
    for a in range(root+1, end+1):
        if lst[a] > lst[root]:
            next_right = a
            break
    func(root+1, next_right-1)
    func(next_right, end)
    print(lst[root])
    

func(0, len(lst)-1)




