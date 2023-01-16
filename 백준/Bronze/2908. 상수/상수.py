arr = list(input().split())
for i in range(2):
    arr[i] = int(arr[i][::-1])
    
v = arr[0]
for num in arr:
    if num > v:
        v = num
print(v)