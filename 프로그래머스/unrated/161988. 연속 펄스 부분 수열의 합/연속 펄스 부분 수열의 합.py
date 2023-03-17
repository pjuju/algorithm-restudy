def solution(sequence):

    for i in range(len(sequence)):
        if i % 2 :
            sequence[i] = sequence[i]
        else:
            sequence[i] = -sequence[i]
    
    answer = sequence[0]
    val = -0xffffffff
    for i in range(len(sequence)):
        if val <= 0:
            val = sequence[i]
        else:
            val += sequence[i]
        if val > answer:
            answer = val
            
    val = -0xffffffff      
    for i in range(len(sequence)):
        if val <= 0:
            val = -sequence[i]
        else:
            val -= sequence[i]
        if val > answer:
            answer = val
            
    print(answer)   
            
            
    return answer