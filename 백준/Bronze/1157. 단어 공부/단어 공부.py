text = input().upper() # 텍스트 입력받아서 바로 대문자화
alpha_list = list(set(text))

max_cnt = 0
max_cnt_idx = 0
max_cnt_num = 0
for i in range(len(alpha_list)):
    alpha_cnt = text.count(alpha_list[i])
    if alpha_cnt > max_cnt:
        max_cnt = alpha_cnt
        max_cnt_idx = i
        max_cnt_num = 1
    elif alpha_cnt == max_cnt:
        max_cnt_num += 1

if max_cnt_num > 1:
    print('?')
else:
    print(alpha_list[max_cnt_idx])