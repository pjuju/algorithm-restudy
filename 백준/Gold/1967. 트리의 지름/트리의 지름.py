import sys
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int,input().split())
    tree[a].append((b,c))



def func():
    result = 0

    for x in range(1,N+1):
        v_l = []
        v = 0
        for i,c in tree[x]:
            cnt = c
            queue = [(i,c)]
            while queue:
                i,c = queue.pop(0)
                if c > cnt:
                    cnt = c
                for ni,nc in tree[i]:
                        queue.append((ni,c+nc))

            v_l.append(cnt)

        v_1 = sorted(v_l, reverse=True)
        for i in range(len(v_l)):
            if i < 2:
                v += v_1[i]
        if v > result:
            result = v

    print(result)





func()





