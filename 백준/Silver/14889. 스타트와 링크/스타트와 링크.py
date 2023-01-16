def group_sum(group):
    sum = 0
    for i in range(len(group)):
        for j in range(len(group)):
            if i != j:
                sum += arr[group[i]][group[j]]
    return sum

def func(idx, selected):
    global result
    if idx == N:
        if sum(selected) == N/2:
            group1 = []
            group2 = []
            for i in range(N):
                if selected[i]:
                    group1.append(person[i])
                else:
                    group2.append(person[i])

            A = group_sum(group1)
            B = group_sum(group2)

            if abs(A-B) < result:
                result = abs(A-B)
        return

    selected[idx] = 1
    func(idx+1, selected)
    selected[idx] = 0
    func(idx+1, selected)


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
person = [i for i in range(N)]
selected = [0] * N
result = 100000000000
func(0,selected)

print(result)