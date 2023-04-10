def solution(players, callings):
    answer = []
    player_num = {}
    for i in range(len(players)):
        player_num[players[i]] = i
    
    for call in callings:
        a_num = player_num[call]
        player_num[call] -= 1
        player_num[players[a_num-1]] += 1
        players[a_num-1], players[a_num] = players[a_num], players[a_num-1]
        
    return players