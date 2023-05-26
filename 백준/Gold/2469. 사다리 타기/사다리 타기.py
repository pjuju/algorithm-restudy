k = int(input())
n = int(input())
start = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:k]
end = list(input())
road = []
r_road = []

flag = True
for i in range(n):
    r = input()
    if r[0] == '?':
        flag = False
    else:
        if flag:
            road.append(list('*' + r + '*'))
        else:
            r_road.append(list('*' + r + '*'))

for r in road:
    for i in range(1, k):
        if r[i] == '-':
            start[i],start[i-1] = start[i-1],start[i]

for ri in range(len(r_road)-1,-1,-1):
    rr = r_road[ri]
    for i in range(1, k):
        if rr[i] == '-':
            end[i],end[i-1] = end[i-1],end[i]
            
result = '*'
for i in range(k-1):    
    if (start[i], start[i+1]) == (end[i+1],end[i]):
        result += '-'
    else:
        result += '*'   

flag = True
for i in range(1, k):
    if result[i] == '-':
        if result[i-1] == '-':
            flag = False
            break
        start[i],start[i-1] = start[i-1],start[i]

if start != end:
    flag = False

if flag:
    print(result[1:])
else:
    print('x' * (k-1))