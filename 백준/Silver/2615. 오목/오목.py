arr = [[0] * 21]+[[0]+list(map(int, input().split()))+[0] for _ in range(19)] + [[0] * 21] #받아오기
# 테두리 두르기
#pprint(arr)
dr = [1,1,1,0]  #위에서 부터 훑어오니까 좌아래, 아래, 우아래, 옆만 보면 됨
dc = [-1,0,1,1]

def solution(arr):
    for r in range(1,20):
        for c in range(1,20):
            if arr[r][c] == 1 or arr[r][c] == 2: # 검은돌이거나 흰돌일 때
                for i in range(4):  # 네 방향을 확인
                    idx_r = r + dr[i]
                    idx_c = c + dc[i]
                    cnt = 1

                    left_idx=[r,c]
                    if arr[r][c] == arr[idx_r][idx_c]: #같은색 돌이 있으면
                        cnt += 1  # 카운트 늘려줌
                        check = True
                        while check: # 같은 방향으로 쭉
                            if 0 <= idx_r <= 20 and 0 <= idx_c <= 20 and arr[idx_r+dr[i]][idx_c+dc[i]] == arr[idx_r][idx_c]:
                                idx_r = idx_r + dr[i]
                                idx_c = idx_c + dc[i]
                                cnt += 1
                                if idx_c < left_idx[1]:
                                    left_idx = [idx_r,idx_c]
                            if 0 <= idx_r <= 20 and 0 <= idx_c <= 20 and cnt == 5 and arr[idx_r+dr[i]][idx_c+dc[i]] == arr[idx_r][idx_c]:
                                check = False  # 5개인데 아래 육목인 경우
                                break
                            if 0 <= r-1 <= 20 and 0 <= c-1 <= 20 and cnt == 5 and arr[r-dr[i]][c-dc[i]] == arr[r][c]:
                                check = False  # 윗쪽 육목인 경우
                                break
                            if 0 <= idx_r <= 20 and 0 <= idx_c <= 20 and cnt == 5:
                                return (arr[r][c], left_idx[0], left_idx[1])  # 오목인 경우
                            if 0 <= idx_r <= 20 and 0 <= idx_c <= 20 and arr[idx_r+dr[i]][idx_c+dc[i]] != arr[idx_r][idx_c]:
                                check = False
                                break
    return 0,0,0
win, R, C = solution(arr)
if win == 0:
    print(0)
else:
    print(win)
    print(R, C)