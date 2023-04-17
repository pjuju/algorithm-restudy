T = int(input())
for tc in range(T):
    sound = input()
    other_sounds = []
    while True:        
        other_sound = input()
        if other_sound[-1] == '?':            
            break
        other_sounds.append(other_sound.split(' goes ')[1])
    result = ''
    for s in sound.split(' '):
        if s not in other_sounds:
            result += (s + ' ') 
    print(result)
    