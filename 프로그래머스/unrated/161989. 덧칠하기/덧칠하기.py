def solution(n, m, section):
    x = 0
    cnt = 0
    for a in section:
        if a > x:
            cnt += 1
            x = a+m-1
    answer = cnt
    return answer