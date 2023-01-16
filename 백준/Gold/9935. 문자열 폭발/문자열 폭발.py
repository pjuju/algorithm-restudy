text = input()
bomb = input()

# while bumb in text:
#     text = text.replace(bumb, '')
# if not text:
#     print("FRULA")
# else:
#     print(text)

stack = []
for char in text:
    stack.append(char)
    if char == bomb[-1]:
        if bomb == "".join(stack[-len(bomb):]):
            # stack = stack[:-len(bomb)]
            del stack[-len(bomb):]

if not stack:
    print("FRULA")
else:
    print("".join(stack))



