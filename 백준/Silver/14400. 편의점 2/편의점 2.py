n = int(input())
r_lst = []
c_lst = []
for _ in range(n):
    c, r = map(int, input().split())
    r_lst.append(r)
    c_lst.append(c)

r_lst.sort()
c_lst.sort()
r = r_lst[n//2]
c = c_lst[n//2]

result = 0
for i in range(n):
    result += abs(r_lst[i]-r)
    result += abs(c_lst[i]-c)

print(result)