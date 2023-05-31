import sys
input = sys.stdin.readline
T = int(input())

def func(idx, val):
    
    global result
    if idx == 11:
        result = max(val, result)
        return
    for p in range(11):
        if lst[idx][p] and not visited[p]:
            visited[p] = 1
            func(idx+1, val+lst[idx][p])
            visited[p] = 0

for tc in range(T):
    lst = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * (11)
    result = 0
    func(0,0)
    print(result)