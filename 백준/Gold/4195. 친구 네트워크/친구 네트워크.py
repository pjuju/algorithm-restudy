import sys
input = sys.stdin.readline


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(a,b):
    pa, pb = find(a), find(b)
    if pa != pb:
        parents[pb] = parents[pa]
        cnts[pa] += cnts[pb]
    print(cnts[pa])


T = int(input())
for _ in range(T):
    F = int(input())
    idxs = dict()
    parents = []
    cnts = []
    i = 0

    for _ in range(F):
        a, b = input().rstrip().split()
        if a not in idxs:
            idxs[a] = i
            parents.append(i)
            cnts.append(1)
            i += 1
            
        if b not in idxs:
            idxs[b] = i
            parents.append(i)
            cnts.append(1)
            i += 1

        union(idxs[a],idxs[b])

