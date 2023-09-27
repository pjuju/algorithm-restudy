'''
(0,0) (0,1) (0,2)'''
arr = [list(map(int, input())) for _ in range(9)]

square_dict = dict()
row_nums = [[0] * 10 for _ in range(9)]
col_nums = [[0] * 10 for _ in range(9)]
for i in range(3):
    for j in range(3):
        square_dict[(i,j)] = [0] * 10

lst = []
for r in range(9):
    for c in range(9):
        if arr[r][c]:
            row_nums[r][arr[r][c]] = 1
            col_nums[c][arr[r][c]] = 1
            rr, cc = r//3, c//3
            square_dict[(rr,cc)][arr[r][c]] = 1
        else:
            lst.append((r,c))


def func(i):
    global result
    if result:
        return
    if i == len(lst):
        result = 1
        for a in arr:
            for n in a:
                print(n, end ='')
            print()
        return
    
    r,c = lst[i]
    for x in range(1, 10):
        if not row_nums[r][x] and not col_nums[c][x]:
            if not square_dict[(r//3, c//3)][x]:
                row_nums[r][x] = col_nums[c][x] = square_dict[(r//3, c//3)][x] = 1
                arr[r][c] = x
                func(i+1)
                row_nums[r][x] = col_nums[c][x] = square_dict[(r//3, c//3)][x] = 0
                arr[r][c] = 0

result = 0
func(0)