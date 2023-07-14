import sys
from collections import deque

input = sys.stdin.readline

n, money = map(int, input().split())
cnt = 0
p = int(input())

for _ in range(n-1):
    np = int(input())
    if np > p:
        amount = money // p
        money += (amount * (np-p))
    
    p = np
print(money)