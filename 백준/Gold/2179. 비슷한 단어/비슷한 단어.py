import sys
input = sys.stdin.readline

N = int(input())
lst = [list(input().rstrip()) for _ in range(N)]
sorted_lst = sorted(lst)
idx_to_sort = {}
sort_to_idx = {}

for i in range(N):
    for j in range(N):
        if sorted_lst[i] == lst[j]:
            sort_to_idx[i] = j
            break

result_cnt = 0
result_lst = [0] * (N)


for i in range(N-1):
    a = sorted_lst[i]
    b = sorted_lst[i+1]

    word = ''
    for k in range(min(len(a), len(b))):
        if a[k] == b[k]:
            word += a[k]
        else:
            break
    
    if len(word) >= result_cnt:
        result_cnt = len(word)
        result_lst[sort_to_idx[i]] = len(word)
        result_lst[sort_to_idx[i+1]] = len(word)

first = 0
word = ''
for i in range(N):
    if result_lst[i] == result_cnt:
        first = i
        word = lst[i][:result_cnt]
        break

second = 1
for j in range(first+1, N):
    if result_lst[i] == result_cnt:
        if lst[j][:result_cnt] == word:
            second = j
            break

print("".join(lst[first]))
print("".join(lst[second]))
            

