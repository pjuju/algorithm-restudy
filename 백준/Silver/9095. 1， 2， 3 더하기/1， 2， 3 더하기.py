def sums(n):
    if 1<= n <= 2:
        return n
    if n==3:
        return n+1
    else:
        return sums(n - 1) + sums(n - 2) + sums(n - 3)  # 규칙을 찾아내는게 중요!

T = int(input())
for tc in range(T):
    n = int(input())
    print(sums(n))