a, b = map(int, input().split())
word = input()
string = input()

wc = [0] * 58
sc = [0] * 58


for i in range(a):
    wc[ord(word[i])-ord('A')] += 1

result = 0
start = 0
length = 0
for i in range(b):
    length += 1
    sc[ord(string[i])-ord('A')] += 1
    
    if length == a:
        if wc == sc:
            result += 1
        
        sc[ord(string[start])-ord('A')] -= 1
        start += 1
        length -= 1

print(result)    
    