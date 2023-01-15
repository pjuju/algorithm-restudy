import sys
input = sys.stdin.readline

N = int(input())

start_index = 1
end_index = 1
count = 0

val = 1
while end_index <= N:

    if val == N:
        count += 1
        end_index += 1
        val += end_index
    
    elif val > N:
        val -= start_index
        start_index += 1
    
    elif val < N:
        end_index += 1
        val += end_index
                
print(count)
    
    
    
    