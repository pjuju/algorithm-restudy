s = input()

sum_val = 0
val = 1
queue = ''
i = 0
while i < len(s):
    if s[i] == '(':
        queue += s[i]
        val *= 2

    elif s[i] == "[":
        queue += s[i]
        val *= 3

    elif s[i] == ')':
        if not queue or queue[-1] == "[":
            sum_val = 0
            break
        if s[i-1] == "(":
            sum_val += val
        queue = queue[:-1]
        val //= 2

    else:
        if not queue or queue[-1] == "(":
            sum_val = 0
            break
        if s[i-1] == "[":
            sum_val += val


        queue = queue[:-1]
        val //= 3
    i += 1


if queue != '':
    sum_val = 0
print(sum_val)
