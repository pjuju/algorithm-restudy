import sys
input = sys.stdin.readline
N, M = map(int, input().split())

single = 0xfffffff
six = 0xfffffff
for _ in range(M):
    x,y = map(int, input().split())
    single, six = min(single,y), min(six,x)

result = min((N+5)//6 * six, (N//6*six + N%6*single),N*single)    
print(result)