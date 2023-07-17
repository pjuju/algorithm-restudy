queue = []
lst = list(input())
result = 0
val = 1
for i in range(len(lst)):
    a = lst[i]

    if a == '(':
        val *= 2
        queue.append(a)
    elif a == '[':
        val *= 3
        queue.append(a)
    
    elif a == ')':
        if not queue or queue[-1] != '(':
            result = 0
            break
        if lst[i-1] == '(':
            result += val    
        queue.pop()
        val //= 2        

    elif a == ']':
        if not queue or queue[-1] != '[':
            result = 0
            break
        if lst[i-1] == '[':
            result += val    
        queue.pop()
        val //= 3

if queue:
    result = 0
print(result)