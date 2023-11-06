N = int(input())


primes = []
prime_check = [1] * (N+1)
for n in range(2, N+1):
    if prime_check[n]:
        primes.append(n)   
    
        for nn in range(n, N+1, n):       
            prime_check[nn] = 0

sub_sums = [0]
for i in range(len(primes)):
    sub_sums.append(sub_sums[-1]+primes[i])

ans = 0

left = 0
right = 0

while right < len(sub_sums):
     
    if sub_sums[right] - sub_sums[left] > N:
        left += 1
    elif sub_sums[right] - sub_sums[left] < N:
        right += 1
    else:
        ans += 1
        right += 1
    
print(ans)
 