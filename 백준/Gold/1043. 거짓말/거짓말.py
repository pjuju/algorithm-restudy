import sys
input = sys.stdin.readline

N, M = map(int, input().split())
knows = list(map(int, input().split()))[1:]
parents = [i for i in range(N+1)]
parties = []

def union(a,b):
    x = find(a)
    y = find(b)
    if x != y:
        parents[y] = x

def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]

result = 0
for _ in range(M):
    party = list(map(int, input().split()))[1:]
    parties.append(party)

for party in parties:
    first = party[0]
    for i in range(1,len(party)):
        union(first,party[i])

for party in parties:
    first = party[0]
    repre = find(first)
    for x in knows:
        if find(x) == repre:
            break
    else:
        result += 1

print(result)