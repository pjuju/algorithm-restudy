text = input()
N = len(text)

def func(x, lst, cnt):
    global result
    if cnt == 2:
        temp = text[:lst[0]][::-1] + text[lst[0]:lst[1]][::-1] + text[lst[1]:][::-1]
        result = min(temp, result)
        return
    for i in range(x+1, N):
        lst.append(i)
        func(i, lst, cnt+1)
        lst.pop()

result = 'z' * N
func(0,[],0)
print(result)
