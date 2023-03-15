def solution(n, left, right):
    result = []
    for i in range(left+1, right+2):
        if i % n == 0:
            result.append(n)
        else:
            result.append(max((i//n)+1,i%n))
    return result