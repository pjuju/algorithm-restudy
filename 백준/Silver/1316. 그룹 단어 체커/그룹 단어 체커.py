N = int(input())
cnt = 0
for _ in range(N):
    text = input()
    now = text[0]
    arr = [text[0]]
    for i in range(len(text)):
        if text[i] != now:
            if text[i] in arr:
                break
            arr.append(text[i])
            now = text[i]
        else:
            pass
    else:
        cnt += 1

print(cnt)