N = int(input())
scores = list(map(int, input().split()))

M = max(scores)

new_sum = 0
for score in scores:
    new_sum += score/M*100

print(new_sum/N)