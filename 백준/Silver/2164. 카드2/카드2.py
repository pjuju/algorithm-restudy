from collections import deque
d = deque()
for i in range(int(input())):
    d.append(i+1)
while len(d) > 1:
    d.popleft()
    d.append(d.popleft())
print(*d)