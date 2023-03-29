led = [[1]*7 for _ in range(10)]
led[0][3] = led[1][0] = led[1][1] = led[1][3] = led[1][4] = led[1][6] = led[2][0] = led[2][5] = led[3][0] = led[3][4] = led[4][1] = led[4][4] = led[4][6] = led[5][2] = led[5][4] = led[6][2] = led[7][0] = led[7][3] = led[7][4] = led[7][6] = led[9][4] = 0

change = [[0] * 10 for _ in range(10)]
for i in range(10):
    for j in range(i,10):
        cnt = 0
        for k in range(7):
            if led[i][k] != led[j][k]:
                cnt += 1
            change[i][j] = cnt
            change[j][i] = cnt

N,K,P,X = map(int, input().split())

X = ((K-len(str(X))) * '0' + str(X))
N = ((K-len(str(N))) * '0' + str(N))

answer = 0
def dfs(tmp, l, cnt):   
    global answer 
    if l == K:
        if tmp != X and int(tmp) > 0:           
            answer += 1
        return

    for x in range(10):
        next_num = tmp+str(x)
        if int(next_num) <= int(N[:l+1]):
            if cnt+change[int(X[l])][x] <= P:
                dfs(tmp+str(x), l+1, cnt+change[int(X[l])][x])
        
dfs('',0,0) # 현재 숫자, 다음 자리, 카운드
print(answer)
    