N = int(input())
arr = [list(input()) for _ in range(N)]
friends = [[] for _ in range(N)]
no_friends = [[] for _ in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        if i != j:
            if arr[i][j] == 'Y':
                friends[i].append(j)
            else:
                no_friends[i].append(j)
            
two_friends = [set() for _ in range(N)]
for i in range(N):
    for no_friend in no_friends[i]:
        for friend in friends[no_friend]:
            if friend in friends[i]:
                two_friends[i].add(no_friend)
                break
    
    tmp = len(two_friends[i]) + len(friends[i]) 
    # print(i, two_friends[i], friends[i])
    if tmp > result:        
        result = tmp

print(result)
                        

