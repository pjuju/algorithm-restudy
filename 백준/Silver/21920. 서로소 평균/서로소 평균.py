N = int(input())
lst = list(map(int, input().split()))
x = int(input())

def gcd(a,b):
    if not b:
        return a
    if b > a:
        a,b = b,a

    return gcd(b,a%b)    

val = 0
cnt = 0
for y in lst:
    if gcd(x,y) == 1:
        val += y
        cnt += 1
        
print(val/cnt)