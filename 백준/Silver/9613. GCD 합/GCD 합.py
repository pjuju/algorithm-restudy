def get_gcd(a,b):
    while b:        
        a, b = b, a%b  

    return a

t = int(input())

for tc in range(t):
    lst = list(map(int, input().split()))
    n = lst[0]
    result = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            result += get_gcd(lst[i], lst[j])
    
    print(result)