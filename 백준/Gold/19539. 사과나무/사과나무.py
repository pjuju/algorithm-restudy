import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

cnt = sum(lst) // 3

if sum(lst) % 3:
    print('NO')

else:
    for n in lst:
        cnt -= (n//2)
    if cnt <= 0 :
        print('YES')
    else:
        print('NO')