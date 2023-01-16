T = int(input())
for tc in range(T):
    lst = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0]*90
    N = int(input())
    for n in range(11,N+1):
        lst[n]=lst[n-5]+lst[n-1]

    print(lst[N])

