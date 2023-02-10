x, y = map(int, input().split())
p = y*100//x
s, e = 0, 1000000000
res = 0
while s <= e:
    m = (s+e)//2
    if (y+m)*100//(x+m) > p:
        e = m-1
        res = m
    else:
        s = m+1
print(res if res != 0 else -1)