N = int(input())


for tc in range(1,1+N):
    S, R = input().split()
    S = int(S)

    result = ''
    for a in R:
        result += a*S

    print(result)