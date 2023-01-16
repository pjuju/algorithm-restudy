def fibo(N):
    if fibo_val[N]:
        return fibo_val[N]

    if N == 0:
        return [1,0]
    if N == 1:
        return [0,1]

    else:
        val = [fibo(N-1)[0] + fibo(N-2)[0], fibo(N-1)[1] + fibo(N-2)[1]]
        fibo_val[N] = val
        return val


T = int(input())
fibo_val = [0]*(41)
for tc in range(T):
    N = int(input())
    print(*fibo(N))