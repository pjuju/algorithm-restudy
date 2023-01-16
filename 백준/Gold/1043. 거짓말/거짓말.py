N,M = map(int, input().split())
truth = list(map(int, input().split()))
check_people = [0] * (N+1)
parties = [list(map(int, input().split()))[1:] for _ in range(M)]
check_parties = [0] * (M+1)
queue = truth[1:]

result = M

for person in queue:
    check_people[person] = 1

while queue:
    person = queue.pop()
    for i in range(M):
        if not check_parties[i]:
            if person in parties[i]:
                result -= 1
                check_parties[i] = 1
                for other_person in parties[i]:
                    if not check_people[other_person]:
                        check_people[other_person] = 1
                        queue.append(other_person)

print(result)





