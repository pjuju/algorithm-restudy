import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dd = set([input().rstrip() for _ in range(N)])
# for _ in range(M):
#     bd = input().rstrip()
#     for d in dd:
#         if d == bd:
#             dd.remove(d)
#             ddbd.append(d)
#             break

bd = set([input().rstrip() for _ in range(M)])
ddbd = list(bd.intersection(dd))
# for d in dd:
#     if d in bd:
#         bd.remove(d)
#         ddbd.append(d)




ddbd.sort()
print(len(ddbd))
for db in ddbd:
    print(db)
