N = int(input())
filenames = [input() for _ in range(N)]

result = ''
for i in range(len(filenames[0])):
    flag = True
    
    for j in range(1, N):
        if filenames[0][i] != filenames[j][i]:
            result += '?'
            flag = False
            break
    
    if flag:
        result += filenames[0][i]

print(result)
