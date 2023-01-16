text = input()

result = 0
num = ''
minus = False

for i in range(len(text)):
    if text[i] in '+-' :
        if text[i] == '-':
            minus = True
        result += int(num)
        if minus:
            num = '-'
        else:
            num = ''

    else:
        num += text[i]

result += int(num)
print(result)