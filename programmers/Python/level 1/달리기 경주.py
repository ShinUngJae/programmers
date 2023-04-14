def solution(players, callings):

    players_name_count = {j : i for i, j in enumerate(players)}
    players_count_name = {i : j for i, j in enumerate(players)}
    for j in callings :
        
        rank = players_name_count[j]
        lose_player = players_count_name[rank - 1]
        
        players_count_name[rank - 1] = j
        players_count_name[rank] = lose_player
        
        players_name_count[lose_player] = rank
        players_name_count[j] = rank - 1
        
    return list(players_count_name.values())