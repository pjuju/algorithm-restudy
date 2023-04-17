def solution(sequence, k):
    result_left = 0
    result_right = len(sequence)
    left = 0
    val = 0
    for right in range(len(sequence)):
        val += sequence[right]
        while val > k:
            val -= sequence[left]
            left += 1
        if val == k:
            if result_right - result_left > right - left:
                result_left, result_right = left, right
    
    return [result_left, result_right]