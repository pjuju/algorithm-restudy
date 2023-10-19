def count(num):  
    cnt = 0  
    bin_num = bin(num)[2:]  
    length = len(bin_num)  
    for i in range(length):  
        if bin_num[i] == '1':  
             
            val = length-i-1  
            cnt += sums[val]  
             
            cnt += (num - 2**val + 1)  
            num = num - 2 ** val  
    return cnt  

x, y = map(int, input().split())  
sums = [0 for _ in range(60)]  

for i in range(1, 60):  
    sums[i] = 2**(i-1) + 2 * sums[i-1]  

print(count(y) - count(x-1))