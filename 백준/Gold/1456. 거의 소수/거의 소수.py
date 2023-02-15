import sys
input = sys.stdin.readline

A,B = map(int, input().split())
max_val = int(B**(1/2))
check = [0] * (max_val+1)
cnt = 0
result = []
for x in range(2, max_val+1):
    if not check[x]:               
        for y in range(x,max_val+1,x):
            check[y] = 1
        
        num = x * x
        while num <= B:
            if num >= A:
                result.append(num)
                cnt += 1
                
            num *= x
            
print(cnt)