H,W = map(int, input().split())
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(i+1, N):
        r1,c1 = lst[i][0],lst[i][1]
        r2,c2 = lst[j][0],lst[j][1]
        for rr1,cc1 in [(r1,c1), (c1,r1)]:
            for rr2, cc2 in [(r2,c2), (c2, r2)]:
                if (rr1+rr2 <= H and max(cc1,cc2) <= W) or (max(rr1,rr2) <= H and cc1+cc2 <= W):
                    if r1*c1 + r2*c2 > result:
                        result = r1*c1 + r2*c2
                    break

print(result)
