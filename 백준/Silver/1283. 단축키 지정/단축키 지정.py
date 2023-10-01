N = int(input())
lst = set()


def func(texts):
    
    for i in range(len(texts)):
        if texts[i][0].lower() not in lst:
            lst.add(texts[i][0].lower())
            texts[i] = '[' + texts[i][0] + ']' + texts[i][1:]
            print(' '.join(texts))
            return
    
    
    for i in range(len(texts)):
        for j in range(len(texts[i])):
            if texts[i][j].lower() not in lst:
                lst.add(texts[i][j].lower())
                texts[i] = texts[i][:j] + '[' + texts[i][j] + ']' + texts[i][j+1:]
                print(' '.join(texts))
                return
    
    print(' '.join(texts))
    return


for _ in range(N):
    command = input().split()
    func(command)


