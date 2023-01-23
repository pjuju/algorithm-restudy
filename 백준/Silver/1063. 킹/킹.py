king, stone, N = input().split()
# i(행),j(열) 범위 = 0~7
king_i = king_j = stone_i = stone_j = 0
king_i += int(ord(king[0])) - ord('A')
stone_i += int(ord(stone[0])) - ord('A')
king_j += int(king[1]) - 1
stone_j += int(stone[1]) - 1

# print(king_i, king_j, stone_i, stone_j)
for _ in range(int(N)):
    movement = input()
    # temp = king_i, king_j
    for move in movement:
        if move == 'L':
            king_i -= 1
        elif move == 'R':
            king_i += 1
        elif move == 'B':
            king_j -= 1
        elif move == 'T':           
            king_j += 1

    if king_i > 7 or king_j > 7 or king_i < 0 or king_j < 0:
        for move in movement:
            if move == 'L':
                king_i += 1
            elif move == 'R':
                king_i -= 1
            elif move == 'B':
                king_j += 1
            elif move == 'T':           
                king_j -= 1

    if (king_i, king_j) == (stone_i, stone_j):
        for move in movement:
            if move == 'L':
                stone_i -= 1
                # king_i += 1
            elif move == 'R':
                stone_i += 1
                # king_i -= 1 
            elif move == 'B':
                stone_j -= 1
                # king_j += 1
            elif move == 'T':           
                stone_j += 1
                # king_j -= 1
        
        if stone_i > 7 or stone_j > 7 or stone_i < 0 or stone_j < 0:
            for move in movement:
                if move == 'L':
                    stone_i += 1
                    king_i += 1
                elif move == 'R':
                    stone_i -= 1
                    king_i -= 1
                elif move == 'B':
                    stone_j += 1
                    king_j += 1
                elif move == 'T':           
                    stone_j -= 1
                    king_j -= 1

king = ''
stone = ''

king += chr(ord('A') + king_i)
king += str(1+king_j)
stone += chr(ord('A') + stone_i)
stone += str(1+stone_j)

print(king)
print(stone)