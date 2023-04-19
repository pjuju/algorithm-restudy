s,N,K,r1,r2,c1,c2 = map(int, input().split())

def func(s,r,c):
    if s == 0:
        return '0'
    if (N-1)/2-K//2 <= r%N <= (N-1)/2+K//2 and (N-1)/2-K//2 <= c%N <= (N-1)/2+K//2:
        return '1'    
    return func(s-1,r//N,c//N)

for r in range(r1,r2+1):
    ans = ''
    for c in range(c1,c2+1):
        ans += func(s,r,c)
    print(ans)