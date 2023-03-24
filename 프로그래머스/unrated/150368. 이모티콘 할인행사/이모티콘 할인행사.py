def solution(users, emoticons):
    ans_cnt = 0
    ans_val = 0
    
    def perm(lst):
        nonlocal ans_cnt, ans_val
        if len(lst) == len(emoticons):
            val = 0
            cnt = 0
            for user in users:
                cost = 0
                for i in range(len(lst)):
                    if lst[i] >= user[0]:
                        cost += ((100-lst[i])/100) * emoticons[i]
                if cost >= user[1]:
                    cnt += 1
                else:
                    val += cost
                    
            if cnt > ans_cnt:
                ans_cnt = cnt
                ans_val = val
            elif cnt == ans_cnt:
                ans_val = max(val,ans_val)
                
            return
        
        for dc in (10,20,30,40):
            lst.append(dc)
            perm(lst)
            lst.pop()
    
    perm([])

    return [ans_cnt, ans_val]