N = int(input())
M = int(input())
lst = [i for i in range(10)]
if M:
    for a in input().split():
        lst.remove(int(a))


def func(x):    
    global result    
    val = len(str(x)) + abs(N-x)
    if len(str(x)) > len(str(N))  and val > result:
        return    
    if val < result:
        result = val    
    if x != 0:
        for y in lst:
            func(int(str(x)+str(y)))
    
now = 100
result = abs(N-now)

for i in lst:        
    func(i)

print(result)