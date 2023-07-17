import sys
input = sys.stdin.readline
import itertools

arr = list(itertools.permutations(['1','2','3','4','5','6','7','8','9'],3))
N = int(input())
cnt = 0

for _ in range(N):
    num,s,b = map(int, input().split())
    num = list(str(num))
    cnt = 0

    for i in range(len(arr)):
        i -= cnt
        strike = ball = 0
        for j in range(3):
            if arr[i][j] == num[j]:
                strike += 1
            elif arr[i][j] in num:
                ball += 1  
    
        if (s != strike) or (b != ball):
            arr.remove(arr[i])
            cnt += 1
            
print(len(arr))