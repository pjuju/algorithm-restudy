num = input()
num_li = []
for i in num:
    num_li.append(int(i))

num_li.sort(reverse=True)

for v in num_li:
    print(v, end='')

