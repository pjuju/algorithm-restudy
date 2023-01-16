import sys
N = int(sys.stdin.readline())
arr_set = set()
for _ in range(N):
    arr_set.add(sys.stdin.readline().rstrip()) # 줄바꿈 요소를 제거해줘야 함

arr=list(arr_set)
arr.sort(key=lambda x: (len(x), x))

for x in arr:
    print(x)
