import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort(key = lambda x:-x[1])

time = 1000000
for amount, until in lst:
    time = min(time, until)
    time -= amount

if time > 0:
    print(time)
else:
    print(-1)