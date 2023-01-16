def dfs(i):
    global cnt
    if i == N:
        cnt += 1
        return
    for j in range(N):
        if not col_check[j] and not dia1[i+j] and not dia2[i-j+N-1]:
            col_check[j] = dia1[i+j] = dia2[i-j+N-1] = 1
            dfs(i+1)
            col_check[j] = dia1[i+j] = dia2[i-j+N-1] = 0


N = int(input())
col_check = [0] * N
dia1 = [0] * (2*N-1) # i+j
dia2 = [0] * (2*N-1) # i-j+N-1
cnt = 0
dfs(0)
print(cnt)
