def part():
    if len(selected) == M:
        print(*selected)
        return

    for num in nums:
        if not num in selected:
            selected.append(num)
            part()
            selected.pop()

N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
selected = []
part()
