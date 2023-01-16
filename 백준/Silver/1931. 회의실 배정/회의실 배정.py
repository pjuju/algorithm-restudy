N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[1],x[0]), reverse=True)

S,E = arr[0]
cnt = 1
for i in range(1,N):
    ss, ee = arr[i]

    if S >= ee:
        cnt += 1

        S, E = ss, ee


    elif S <= ss:
        S, E = ss, ee


print(cnt)


