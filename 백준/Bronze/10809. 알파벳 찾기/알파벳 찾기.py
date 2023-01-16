alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# alt키로 편하게 입력가능
alpha_idx = [-1] * len(alpha)

text = input()
for i in range(len(alpha)):
    for j in range(len(text)):
        if alpha[i] == text[j]:
            alpha_idx[i] = j
            break


print(*alpha_idx)