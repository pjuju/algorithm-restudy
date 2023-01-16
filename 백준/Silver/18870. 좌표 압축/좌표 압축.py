
import sys
N = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))

arr_2 = list(sorted(set(arr)))

result_dict = {}

for i in range(len(arr_2)):
    result_dict[arr_2[i]] = i

for x in arr:
    print(result_dict[x], end=' ')
