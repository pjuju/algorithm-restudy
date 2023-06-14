import sys
input = sys.stdin.readline

N = int(input())


def func(cnt):
    if cnt == len(text):
        print(''.join(lst))
        return

    for t in visited:
        if visited[t]:
            visited[t] -= 1
            lst.append(t)
            func(cnt+1)
            visited[t] += 1
            lst.pop()
            

for _ in range(N):
    text = sorted(list(input().strip()))
    lst = []
    visited = {}
    for t in text:
        if t in visited:
            visited[t] += 1
        else:
            visited[t] = 1
    func(0)
