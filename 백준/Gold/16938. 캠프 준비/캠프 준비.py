import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
scores = list(map(int, input().split()))

scores.sort()


def func(si, idx, val):
    global result
    if L <= val <= R:
        if scores[idx] - scores[si] >= X:
            result += 1

    for i in range(idx+1, N):        
        func(si, i, val+scores[i])

result = 0
for i in range(N):
    func(i, i, scores[i])

print(result)