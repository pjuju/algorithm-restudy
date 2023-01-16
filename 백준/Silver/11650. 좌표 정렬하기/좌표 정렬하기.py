import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    val = list(map(int,sys.stdin.readline().split()))
    arr.append(val)

new_arr = arr.sort(key=lambda x: (x[0], x[1]))


for val in arr:
    print(val[0],val[1])


