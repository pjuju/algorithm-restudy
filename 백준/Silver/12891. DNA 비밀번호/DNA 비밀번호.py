P, S = map(int, input().split())
word = input()
check = list(map(int, input().split()))
my_check = [0] * 4
result = 0

def plus_alpha(x):
    if x == 'A':
        my_check[0] += 1
    elif x == 'C':
        my_check[1] += 1
    elif x == 'G':
        my_check[2] += 1
    elif x == 'T':
        my_check[3] += 1

def minus_alpha(x):
    if x == 'A':
        my_check[0] -= 1
    elif x == 'C':
        my_check[1] -= 1
    elif x == 'G':
        my_check[2] -= 1
    elif x == 'T':
        my_check[3] -= 1
        
def check_pass():
    global result
    for i in range(4):
        if my_check[i] < check[i]:
            return 
    result += 1

for i in range(S):
    plus_alpha(word[i])

left = 0
check_pass()

for x in range(P-S):
    minus_alpha(word[left])
    left += 1
    plus_alpha(word[left+S-1])
    check_pass()
    
print(result)


    
    



 
     

