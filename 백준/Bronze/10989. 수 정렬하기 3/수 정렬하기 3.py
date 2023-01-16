import sys
input=sys.stdin.readline

n = int(input().rstrip())
num = [0] * 10001

for _ in range(n):
    a = int(input().rstrip())
    num[a] += 1
    

for i in range(1, 10001):
    if num[i] != 0:
        for j in range((num[i])):
            print(i)