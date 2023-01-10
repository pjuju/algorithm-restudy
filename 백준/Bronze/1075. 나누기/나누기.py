N = input()
F = int(input())
n_left = N[:-2]

for n_right in range(100):
    if n_right < 10:
        n_right = '0' + str(n_right)
    
    if int(n_left + str(n_right)) % F == 0:
        print(n_right)
        break

