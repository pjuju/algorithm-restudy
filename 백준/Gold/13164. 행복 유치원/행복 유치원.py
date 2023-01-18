import sys
input = sys.stdin.readline

N, K= map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
minus = sorted([arr[i+1]-arr[i] for i in range(N-1)])
print(sum(minus[:N-K]))