import sys
sys.setrecursionlimit(20000)
N = int(input())

def func(val, i):   

    while not val%10:
        val //= 10 

    val %= 10000000
    if i == N:
        print(str(val)[-1])
        return
    
    func(val*(i+1), i+1)

func(1,1)
